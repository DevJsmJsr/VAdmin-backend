from django.db import connection, models
from django.db.models.query import QuerySet
from django.utils import timezone


class SoftDeletionQuerySet(QuerySet):
  """
  The SoftDeletionQuerySet class overrides the delete method to prevent permanent data deletion.
  """

  def delete(self):
    """
    Updates the status to 'deleted'.
    :param delete_by: int - ID of the user performing the deletion
    :return: QuerySet
    """
    return super(SoftDeletionQuerySet, self).update(
      date_deleted=timezone.now(),
      state=False
    )

  def hard_delete(self):
    """
    Deletes the data.
    :return: QuerySet
    """

    return super(SoftDeletionQuerySet, self).delete()

  def truncate(self, cascade=False):
    appendix = " CASCADE;" if cascade else ";"
    raw_sql = f"TRUNCATE TABLE {self.model._meta.db_table}{appendix}"
    with connection.cursor() as cursor:
      cursor.execute(raw_sql)


class SoftDeletionManager(models.Manager):
  """
  The SoftDeletionManager class is used to manage updates performed by the user.
  """

  _queryset_class = SoftDeletionQuerySet

  def __init__(self, *args, **kwargs):
    """
    Initialize with the alive_only parameter with True to ensure that you
    only get active state objects.
    :param args:
    :param kwargs:
    """

    self.alive_only = kwargs.pop('alive_only', True)
    super(SoftDeletionManager, self).__init__(*args, **kwargs)

  def get_queryset(self):
    """
    Gets all active objects and without deleted date.
    :return: QuerySet
    """

    if self.alive_only:
      return self._queryset_class(self.model).filter(
        state=True, date_deleted=None
      )
    return self._queryset_class(self.model)

  def hard_delete(self):
    """
    Created method hard_delete to QuerySet.
    :return: QuerySet
    """

    return self.get_queryset().hard_delete()

  def truncate(self):
    return self.get_queryset().truncate()


class Auditor(models.Model):
  """
  Abstract class to generate audit fields.
  """

  date_created = models.DateTimeField(auto_now_add=True,
                                      help_text='date created')
  date_updated = models.DateTimeField(null=True,
                                      auto_now=True,
                                      help_text='date updated')
  date_deleted = models.DateTimeField(help_text='date deleted', null=True,
                                      blank=True)
  state = models.BooleanField(default=True, help_text='status')
  objects = SoftDeletionManager()
  all_objects = SoftDeletionManager(alive_only=False)

  class Meta:
    abstract = True
    ordering = ['-date_created']

  def delete(self, using=None, keep_parents=False):
    """
    Overrides delete method to avoid delete data.
    :param deleted_by:int
    :return: None
    """

    self.state = False
    self.date_deleted = timezone.now()
    self.save()

  def hard_delete(self):
    """
    Used to delete data.
    :param using:str
    :return: Auditor
    """

    return super(Auditor, self).delete()

  def truncate(self, cascade=False):
    appendix = " CASCADE;" if cascade else ";"
    raw_sql = f"TRUNCATE TABLE {self.model._meta.db_table}{appendix}"
    with connection.cursor() as cursor:
      cursor.execute(raw_sql)


  def __str__(self):
    return "{}".format(self.pk)

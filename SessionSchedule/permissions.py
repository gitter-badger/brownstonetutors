from django.core.exceptions import ObjectDoesNotExist
def calendar_permissions(ob, user):
	if user.is_authenticated():
		try:
			profile = user.base_profile
		except ObjectDoesNotExist:
			return user.is_superuser
		else:
			return (user.is_superuser) or (ob.pk == profile.calendar.pk)
	return False

def event_permissions(ob, user):
	is_creator = (ob is None)
	if is_creator:
		return True
	else:
		is_creator = (ob.creator is not None)
		if is_creator:
			is_creator = (user.pk == ob.creator.pk)
	return (user.is_superuser or is_creator)
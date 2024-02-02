from django.http import HttpResponseRedirect

def unblock_user_view(request, user_id):
  """Unblocks a user from a user's profile page."""

  user = User.objects.get(pk=user_id)
  blocked_user = User.objects.get(pk=request.POST['blocked_user_id'])

  unblock_user(user, blocked_user)

  return HttpResponseRedirect(user.get_absolute_url())
  
  

from django.contrib.auth.models import User

def get_blocked_user_ids(user):
  """Returns a list of all blocked user IDs."""

  blocked_users = user.blocked_by.all()
  blocked_user_ids = []

  for blocked_user in blocked_users:
    blocked_user_ids.append(blocked_user.id)

  return blocked_user_ids
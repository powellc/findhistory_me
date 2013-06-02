# Views here are heavily modified from traditional Django views
# Instead of using the ORM, we're going to hack up a Riak interface
# So that artifact data is stored there instead of the default DB
import riak
import uuid
import time
import urllib

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from riak_crud import get_artifact, create_artifact


class CreateArtifactView(CreateView):
    def post(self, request, *args, **kwargs):
        if self.form.is_valid():
            encoded_image = urllib.quote(open(self.form.image.url, "rb").read().encode("base64"))
            artifact_dict = {
                'title': self.form.title,
                'description': self.form.description,
                'address': self.form.address,
                'city': self.form.city,
                'state': self.form.state,
                'zipcode': self.form.zipcode,
                'image': encoded_image,
                'created': time.time(),
                'updated': time.time(),
                'created_by': request.user.username,
            }
            create_artifact(artifact_dict)

class UpdateArtifactView(CreateView):
    def post(self, request, *args, **kwargs):
        if self.form.is_valid():
            artifact_dict = {}
            if self.form.title:
                artifact_dict['title'] = self.form.title

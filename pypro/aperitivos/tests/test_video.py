import pytest
from django.urls import reverse

from pypro.aperitivos.models import Video
from pypro.django_assertions import assert_contains

# Create your tests here.
@pytest.fixture
def video(db):
    v = Video(slug='motivacao', titulo='Video Aperitivo: Motivação', vimeo_id='251224475')
    v.save()
    return v


@pytest.fixture
def resp(client, video):
    return client.get(reverse('aperitivos:video', args=(video.slug,)))

def test_status_code(resp):
    assert resp.status_code == 200

def test_titulo_video(resp, video):
    assert_contains(resp, video.titulo)

def test_conteudo_video(resp, video):
    assert_contains(resp, video.vimeo_id)
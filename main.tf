terraform {
  required_providers {
    docker = {
      source = "kreuzwerker/docker"
      version = "3.0.2"
    }
  }
}

provider "docker" {
  # Configuration options
}

resource "docker_image" "django_app" {
  name = "django-app-image"
  build {
    context = "./"
  }
}

resource "docker_container" "django_app_container" {
  name  = "django-app-container"
  image = docker_image.django_app.image_id

  ports {
    internal = 8000
    external = 8000
  }
}

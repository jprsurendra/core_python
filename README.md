# Understanding classes and objects/instances

In object-oriented terminology, a class is a template for defining objects. It may contains some variables that can exist in an object, as well as "methods"--procedures for operating on those variables. 

A class can be thought of as a `"type"`, with the objects(or instances) being a `"variable"` of that type. 

Multiple objects/instances of a class can be created in a single program, just like you declare multiple variables of the same type (int, string etc...) in any program.








# Django Taggit Rest Serializer

[![Build Status](https://travis-ci.org/glemmaPaul/django-taggit-serializer.svg?branch=master)](https://travis-ci.org/glemmaPaul/django-taggit-serializer)

## About
This package is meant for the `django-taggit` package which is available [here](https://github.com/alex/django-taggit)

The `django-taggit` package makes it possible to tag a certain module.

## Installation
To install this package you can use the following `pip` installation:
```
pip install django-taggit-serializer
```

Then, add `taggit_serializer` to your `Settings` in `INSTALLED_APPS`:
```
    INSTALLED_APS = (
        ...
        'taggit_serializer',
    )
```

## Usage
Because the tags in `django-taggit` need to be added into a `TaggableManager()` we cannot use the usual `Serializer` that we get from Django REST Framework. Because this is trying to save the tags into a `list`, which will throw an exception.

To accept tags through a `REST` API call we need to add the following to our `Serializer`:
```python
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)


class YourSerializer(TaggitSerializer, serializers.ModelSerializer):

    tags = TagListSerializerField()

    class Meta:
        model = YourModel
```

And you're done, so now you can add tags to your model

## Contribute

Please feel free to create pull requests and issues!
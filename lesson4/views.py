from django.http import HttpRequest, HttpResponse

# from lesson2.models import Person, PersonProfile


def making_queries(request: HttpRequest) -> HttpResponse:
    # Person.objects.create(
    #     first_name='someone'
    # )
    # print(person)
    # print([person])
    # person = Person(first_name='someone')
    # person.last_name = 'someone_last_name'
    # if person.last_name == 'someone_last_name':
    #     person.first_name = 'one_one'
    # person.save()
    # PersonProfile.objects.create(
    #     height=324,
    #     photo='photos/1.jpg',
    #     owner_id=12
    # )
    return HttpResponse('content')

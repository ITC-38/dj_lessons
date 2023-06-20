# from django.db.models import QuerySet
# from django.http import HttpRequest, HttpResponse
# from django.shortcuts import get_object_or_404, render

# from lesson2.models import Person, Authors, Books


# from lesson2.models import Person, PersonProfile


# def making_queries(request: HttpRequest, id: str) -> HttpResponse:
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
    # users: list[Person] = Person.objects.all()
    # render_response = ''
    # for user in users:
    #     render_response += f'<h2>ID: {user.pk}</h2>' \
    #                        f'<p>Полное имя: {user.first_name + " " + user.last_name}</p>' \
    #                        f'<p>Дата обновление профиля: {user.last_update}</p>' \
    #                        f'<p>Дата создания аккаунта: {user.registration_date}</p><br>'
    # user = Person.objects.get(pk=id)
    # user = get_object_or_404(Person, first_name=id)
    # users = Authors.objects.prefetch_related('author_books')
    # print(users.query)
    # for user in users.all():
    #     print(user.author_books.all())
    # books = Books.objects.select_related('author').all()
    # for book in books:
    #     print(book.author.full_name)
    # print(books.query)
    # books = books.all()
    # print(books)
    # print(user.query)
    # user = user.first()
    # print(user)
    # if not user:
    #     return HttpResponse('404 not found')
    # render_response = f'<h2>ID: {user.pk}</h2>' \
    #                   f'<p>Полное имя: {user.first_name + " " + user.last_name}</p>' \
    #                   f'<p>Дата обновление профиля: {user.last_update}</p>' \
    #                   f'<p>Дата создания аккаунта: {user.registration_date}</p><br>'
    # render_response: QuerySet = Authors.objects.prefetch_related('author_books')
    # print(render_response.query)
    # render_response = render_response.author_books.all()
    # return render(request, 'lesson4/test.html')

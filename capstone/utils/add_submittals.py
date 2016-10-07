from mixer.backend.django import mixer


def create_end_users(amount):
    counter = 0
    for i in range(amount+1):
        person = mixer.blend('submittals.Person')
        person.save()
        print("Person #{}...".format(counter))

        submittal = mixer.blend('submittals.Submittal', loan_processor=person)
        submittal.save()
        print("Submitall #{}...".format(counter))
        counter += 1
    return "Done!"


def create_user_with_submittals(amount):
    username = 'Andre'
    password = 'password123'
    user = mixer.blend('auth.User', username=username, password=password)
    user.save()
    person = mixer.blend('submittals.Person', user=user)
    person.save()
    print("User {} created...Password {} created...".format(username, password))

    counter = 0
    for i in range(amount + 1):
        submittal = mixer.blend('submittals.Submittal', loan_processor=person)
        submittal.save()
        print("Submitall #{}...".format(counter))
        counter += 1
    return "Done!"

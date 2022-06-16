def yetki_sorgulama(page):

    def inner(role):
        if role == "admin" or role == "Admin":
            print(f"{role} can reach this {page}")
        else:
            print(f"{role} cannot reach this {page}")
    return inner
roleInput = input()
pageInput = input()
adm = yetki_sorgulama(pageInput)
adm(roleInput)
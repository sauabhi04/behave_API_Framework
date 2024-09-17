__base_uri: str = "https://gorest.co.in/"
__base_path: str = "/public/v2/users"
API_ENDPOINT: str = __base_uri + __base_path


def add_query_param(name, email, status, gender):
    if name == "" and email == "" and status == "" and gender == "":
        return ""
    elif name == "" and email == "" and status == "":
        return "?gender={}".format(gender)
    elif name == "" and email == "" and gender == "":
        return "?status={status}"
    elif name == "" and status == "" and gender == "":
        return "?email={email}"
    elif email == "" and status == "" and gender == "":
        return "?name={name}"

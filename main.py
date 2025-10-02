from pyscript import when, display, document

@when("click", "#submit-btn")
def show_message(event):
    name = document.querySelector("#name").value
    age = document.querySelector("#age").value
    hobbies = document.querySelector("#hobbies").value

    # Clear the output div first
    document.querySelector("#output").innerText = ""

    # Multiline message using input values
    message = f"""👤 My Profile
    Name   : {name}
    Age    : {age}
    Hobbies : {hobbies}

    ✏️ Notes Info:
    {name} is currently {age} years old and their hobbies are {hobbies}.
    This information was gathered through input fields and displayed using
    a multiline string in Python via PyScript.
    """

    display(message, target="output")




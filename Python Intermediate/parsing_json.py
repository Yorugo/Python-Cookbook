import json


def part1():
    people_string = """
    {
      "people": [
        {
          "name": "John Smith",
          "phone": "123-456-789",
          "emails": [
            "johnsmith@bogusemail.com",
            "john.smith@work-place.com"
          ],
          "has_licence": false
        },
        {
          "name": "Jane Doe",
          "phone": "987-654-321",
          "emails": null,
          "has_licence": true
        }
      ]
    }
    """

    data = json.loads(people_string)
    print(type(data))  # dict
    print(data["people"][0]["phone"])
    for person in data["people"]:
        print(person["name"])

    for person in data["people"]:
        del person["phone"]

    new_string = json.dumps(data, indent=2, sort_keys=True)
    print(new_string)  # new json string without phone numbers


def part2():
    with open("states.json") as f:
        data = json.load(f)

    for state in data["states"]:
        print(f"{state['name']}, {state['abbreviation']}")
        del state["area_codes"]

    with open("new_states.json", "w") as f:
        json.dump(data, f, indent=2)

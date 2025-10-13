"""
Acquaintance group structure
"""

my_group = [
    {
        "id": 1,  # Unique ID, because name is not unique
        "name": "Jill",
        "age": 26,
        "job": "biologist",
        "connections": [
            {"id": 2, "connection": "friend"},
        ]
    },
    {
        "id": 2,
        "name": "Zalika",
        "age": 28,
        "job": "artist",
        "connections": [
            {"id": 1, "connection": "friend"},
        ]
    },
    {
        "id": 3,
        "name": "John",
        "age": 27,
        "job": "writer",
        "connections": [
            {"id": 2, "connection": "partner"},
        ]
    },
    {
        "id": 4,
        "name": "Nash",
        "age": 34,
        "job": "chef",
        "connections": [
            {"id": 2, "connection": "landlord"},
            {"id": 3, "connection": "cousin"},
        ]
    },
    {
        "id": 5,
        "name": "jerry",
        "age": 35,
        "job": "ceo",
        "connections": []
    },
]


def get_name_by_id(group_list, param):
    for person in group_list:
        if person.get("id") == param:
            return person.get("name")
    return "Unknown"


def display_group(group_list):
    for person in group_list:
        name = person.get("name")
        age = person.get("age")
        # Handle cases where 'job' is None or not present, for 'no job' consideration
        job = person.get("job") if person.get("job") else "Unemployed"
        connections = person.get("connections", [])

        # 1. Output basic information
        print(f"\n--- {name} (ID: {person['id']}) ---")
        print(f"  Age: {age}")
        print(f"  Job: {job}")

        # 2. Output connections
        if connections:
            print("  Connections:")
            for conn in connections:
                other_name = get_name_by_id(group_list, conn.get("id"))
                rel_type = conn.get("connection")
                print(f"    - Considers {other_name}'s {rel_type}")
        else:
            # Handle no connections
            print("  No connections.")


def average_age():
    """Calculate the average age of the group"""
    global my_group
    if not my_group:
        return 0

    total_age = sum(person.get("age", 0) for person in my_group)
    return total_age / len(my_group)


def forget(person1, person2):
    """Remove the connection between two people in the group"""
    global my_group
    # Get the IDs of the two people
    id1 = None
    id2 = None

    for person in my_group:
        if person.get("name") == person1:
            id1 = person.get("id")
        if person.get("name") == person2:
            id2 = person.get("id")

    # Return False if either person is not found
    if id1 is None or id2 is None:
        return False

    # Remove person2 from person1's connections
    for person in my_group:
        if person.get("id") == id1 and person.get("connections"):
            person["connections"] = [conn for conn in person["connections"]
                                     if conn.get("id") != id2]

    # Remove person1 from person2's connections
    for person in my_group:
        if person.get("id") == id2 and person.get("connections"):
            person["connections"] = [conn for conn in person["connections"]
                                     if conn.get("id") != id1]

    return True


def add_person(name, age, job, relations=None):
    """Add a new person with the given characteristics to the group"""
    global my_group
    if relations is None:
        relations = []

    # Find the maximum ID and add 1 as the new ID
    max_id = max(person.get("id", 0) for person in my_group) if my_group else 0
    new_id = max_id + 1

    # Create a new person object
    new_person = {
        "id": new_id,
        "name": name,
        "age": age,
        "job": job,
        "connections": relations
    }

    # Add to the group
    my_group.append(new_person)
    return new_id


if __name__ == '__main__':
    avg = average_age()
    print(f"Average age of the group: {avg:.2f}")

    print("Removing connection between Jill and Zalika...")
    success = forget("Jill", "Zalika")
    if success:
        print("Successfully removed connection")
        display_group(my_group)
    else:
        print("Failed to remove connection")

    print("Adding a new person")
    new_id = add_person("chenfanghang", 25, "student", [{"id": 1, "connection": "classmate"}])
    display_group(my_group)

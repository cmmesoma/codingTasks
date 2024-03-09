class Email:
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    def mark_as_read(self):
        self.has_been_read = True

# Initialise an empty list to store email objects
inbox = []

def populate_inbox():
    # Sample emails to populate the inbox
    sample_emails = [
        Email("sender1@example.com", "Welcome to HyperionDev!", "Thank you for joining."),
        Email("sender2@example.com", "Great work on the bootcamp!", "Your progress is impressive."),
        Email("sender3@example.com", "Your excellent marks!", "Congratulations on your achievements.")
    ]
    # Add sample emails to the inbox
    inbox.extend(sample_emails)

def list_emails():
    if not inbox:
        print("Inbox is empty.")
    else:
        print("Inbox:")
        for index, email in enumerate(inbox):
            status = "Unread" if not email.has_been_read else "Read"
            print(f"{index} [{status}] {email.subject_line}")

def read_email(index):
    if 0 <= index < len(inbox):
        email = inbox[index]
        if not email.has_been_read:
            print("\nNew Email:")
            print(f"From: {email.email_address}")
            print(f"Subject: {email.subject_line}")
            print("----------")
            print(email.email_content)
            print("----------")
            email.mark_as_read()
            print(f"\nEmail from {email.email_address} marked as read.\n")
        else:
            print("\nEmail already read.")
    else:
        print("\nInvalid email index.")

# Populate inbox with sample emails at startup
populate_inbox()

# Main menu loop
while True:
    print("\nMain Menu:")
    print("1. Read an email")
    print("2. View unread emails")
    print("3. Quit application")

    choice = input("Enter your choice: ")

    if choice == "1":
        list_emails()
        email_index = int(input("Enter the index of the email you want to read: "))
        read_email(email_index)
    elif choice == "2":
        list_emails()
    elif choice == "3":
        print("Quitting application. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
        
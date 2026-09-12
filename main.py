from src.password_remover import remove_pdf_password


def main():
    print("=" * 50)
    print("     PASSWORD PROTECTED PDF REMOVER")
    print("=" * 50)

    input_file = input("Enter input PDF path: ")
    password = input("Enter PDF password: ")
    output_file = input("Enter output PDF path: ")

    success, message = remove_pdf_password(
        input_file,
        output_file,
        password
    )

    if success:
        print(f"\n✅ {message}")
        print(f"Output file: {output_file}")
    else:
        print(f"\n❌ {message}")


if __name__ == "__main__":
    main()
# noinspection PyClassHasNoInit
class Settings:

    input_files = '../materials/*.csv'
    output_dir = './odoofied'

    force_override = True

    file_columns = {
        'apartments': [
            #
            (0, 'apartment.apartment_{}'),  # Apt ID
            (1, False),  # Address
            (2, False),  # Sq. meters
            (3, False),  # Balance (EUR)
            (4, 'apartment.user_{}'),  # User ID
        ],
        'users': [
            (0, 'apartment.user_{}'),  # User ID
            (1, False),  # First Name
            (2, False),  # Last name
            (3, False),  # Email
        ]
    }

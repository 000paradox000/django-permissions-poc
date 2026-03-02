# Django Permissions

This is a PoC to test django-guardian.

## Models

### OperatingSystem

| Field | Type         | Foreign Key |
|-------|--------------|-------------|
| name  | CharField    |             |

| Name      |
|-----------|
| GNU/Linux |
| Windows   |
| Mac OS    |

### Distribution

| Field             | Type       | Foreign Model   |
|-------------------|------------|-----------------|
| name              | CharField  |                 |
| operating_system  | ForeignKey | OperatingSystem |

| Name       | Operating System |
|------------|------------------|
| Debian     | GNU/Linux        |
| Ubuntu     | GNU/Linux        |
| Windows 11 | Windows          |
| Windows XP | Windows          |
| Sequoia    | Mac OS           |
| Monterrey  | Mac OS           |

## Permissions

- [X] Add
- [X] Change
- [X] Delete
- [X] View
- [X] View All

## Groups

- [X] SuperAdmin: virtual group, is_superuser & is_staff
- [ ] Operating System Viewer: Can view, view all OperatingSystem
- [ ] Operating System Admin: Can add, change, delete, view, view all OperatingSystem
- [ ] Operating System Owner: Can add, change, delete, view, view all OperatingSystem owned by the user
- [ ] Distribution Viewer: Can view, view all Distribution
- [ ] Distribution Admin: Can add, change, delete, view, view all Distribution
- [ ] Distribution Owner: Can add, change, delete, view, view all Distribution owned by the user

### Anonymous

| Status | Model           | Permission                                | Has permission | Owned only |
|--------|-----------------|-------------------------------------------|----------------|------------|
| [ ]    | OperatingSystem | operating_systems.add_operatingsystem     | False          | False      |
| [ ]    | OperatingSystem | operating_systems.change_operatingsystem  | False          | False      |
| [ ]    | OperatingSystem | operating_systems.delete_operatingsystem  | False          | False      |
| [ ]    | OperatingSystem | operating_systems.view_operatingsystem    | False          | False      |
| [ ]    | OperatingSystem | operating_systems.viewall_operatingsystem | False          | False      |
| [ ]    | Distribution    | operating_systems.add_distribution        | False          | False      |
| [ ]    | Distribution    | operating_systems.change_distribution     | False          | False      |
| [ ]    | Distribution    | operating_systems.delete_distribution     | False          | False      |
| [ ]    | Distribution    | operating_systems.view_distribution       | False          | False      |
| [ ]    | Distribution    | operating_systems.viewall_distribution    | False          | False      |

### Super Admin

| Status | Model           | Permission                                | Has permission | Owned only |
|--------|-----------------|-------------------------------------------|----------------|------------|
| [ ]    | OperatingSystem | operating_systems.add_operatingsystem     | True           | False      |
| [ ]    | OperatingSystem | operating_systems.change_operatingsystem  | True           | False      |
| [ ]    | OperatingSystem | operating_systems.delete_operatingsystem  | True           | False      |
| [ ]    | OperatingSystem | operating_systems.view_operatingsystem    | True           | False      |
| [ ]    | OperatingSystem | operating_systems.viewall_operatingsystem | True           | False      |
| [ ]    | Distribution    | operating_systems.add_distribution        | True           | False      |
| [ ]    | Distribution    | operating_systems.change_distribution     | True           | False      |
| [ ]    | Distribution    | operating_systems.delete_distribution     | True           | False      |
| [ ]    | Distribution    | operating_systems.view_distribution       | True           | False      |
| [ ]    | Distribution    | operating_systems.viewall_distribution    | True           | False      |

### Operating System Viewer Admin

| Status | Model           | Permission                                | Has permission | Owned only |
|--------|-----------------|-------------------------------------------|----------------|------------|
| [ ]    | OperatingSystem | operating_systems.add_operatingsystem     | False          | False      |
| [ ]    | OperatingSystem | operating_systems.change_operatingsystem  | False          | False      |
| [ ]    | OperatingSystem | operating_systems.delete_operatingsystem  | False          | False      |
| [ ]    | OperatingSystem | operating_systems.view_operatingsystem    | True           | False      |
| [ ]    | OperatingSystem | operating_systems.viewall_operatingsystem | True           | False      |
| [ ]    | Distribution    | operating_systems.add_distribution        | False          | False      |
| [ ]    | Distribution    | operating_systems.change_distribution     | False          | False      |
| [ ]    | Distribution    | operating_systems.delete_distribution     | False          | False      |
| [ ]    | Distribution    | operating_systems.view_distribution       | False          | False      |
| [ ]    | Distribution    | operating_systems.viewall_distribution    | False          | False      |





| Status | Model            | Permission                                | Owned only |
|--------|------------------|-------------------------------------------|------------|
| [ ]    | OperatingSystem  | operating_systems.view_operatingsystem    | False      |
| [ ]    | OperatingSystem  | operating_systems.viewall_operatingsystem | False      |

### Operating System Admin

| Status | Model            | Permission                                |
|--------|------------------|-------------------------------------------|
| [ ]    | OperatingSystem  | operating_systems.add_operatingsystem     |
| [ ]    | OperatingSystem  | operating_systems.change_operatingsystem  |
| [ ]    | OperatingSystem  | operating_systems.delete_operatingsystem  |
| [ ]    | OperatingSystem  | operating_systems.view_operatingsystem    |
| [ ]    | OperatingSystem  | operating_systems.viewall_operatingsystem |

## Users

| Status | Username      | Password  | Group                    |
|--------|---------------|-----------|--------------------------|
| [ ]    | admin         | 12345     | SuperAdmin               |
| [ ]    | os_viewer     | 12345     | Operating System Viewer  |
| [ ]    | os_admin      | 12345     | Operating System Admin   |
| [ ]    | os_owner      | 12345     | Operating System Owner   |
| [ ]    | distro_viewer | 12345     | Distribution Viewer      |
| [ ]    | distro_admin  | 12345     | Distribution Admin       |
| [ ]    | distro_owner  | 12345     | Distribution Owner       |

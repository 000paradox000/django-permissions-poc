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

| Name                           | App Label         | Codename                | Permission full name                      |
|--------------------------------|-------------------|-------------------------|-------------------------------------------|
| Can add operating system       | operating_systems | add_operatingsystem     | operating_systems.add_operatingsystem     |
| Can change operating system    | operating_systems | change_operatingsystem  | operating_systems.change_operatingsystem  |
| Can delete operating system    | operating_systems | delete_operatingsystem  | operating_systems.delete_operatingsystem  |
| Can view operating system      | operating_systems | view_operatingsystem    | operating_systems.view_operatingsystem    |
| Can view all operating systems | operating_systems | viewall_operatingsystem | operating_systems.viewall_operatingsystem |
| Can add distribution           | operating_systems | add_distribution        | operating_systems.add_distribution        |
| Can change distribution        | operating_systems | change_distribution     | operating_systems.change_distribution     |
| Can delete distribution        | operating_systems | delete_distribution     | operating_systems.delete_distribution     |
| Can view distribution          | operating_systems | view_distribution       | operating_systems.view_distribution       |
| Can view all distributions     | operating_systems | viewall_distribution    | operating_systems.viewall_distribution    |

## Groups or User Roles

### Anonymous

| Model           | Permission full name                      | Has permission | Owned only |
|-----------------|-------------------------------------------|----------------|------------|
| OperatingSystem | operating_systems.add_operatingsystem     | False          | False      |
| OperatingSystem | operating_systems.change_operatingsystem  | False          | False      |
| OperatingSystem | operating_systems.delete_operatingsystem  | False          | False      |
| OperatingSystem | operating_systems.view_operatingsystem    | False          | False      |
| OperatingSystem | operating_systems.viewall_operatingsystem | False          | False      |
| Distribution    | operating_systems.add_distribution        | False          | False      |
| Distribution    | operating_systems.change_distribution     | False          | False      |
| Distribution    | operating_systems.delete_distribution     | False          | False      |
| Distribution    | operating_systems.view_distribution       | False          | False      |
| Distribution    | operating_systems.viewall_distribution    | False          | False      |

### SuperAdmin

| Model           | Permission full name                      | Has permission | Owned only |
|-----------------|-------------------------------------------|----------------|------------|
| OperatingSystem | operating_systems.add_operatingsystem     | True           | False      |
| OperatingSystem | operating_systems.change_operatingsystem  | True           | False      |
| OperatingSystem | operating_systems.delete_operatingsystem  | True           | False      |
| OperatingSystem | operating_systems.view_operatingsystem    | True           | False      |
| OperatingSystem | operating_systems.viewall_operatingsystem | True           | False      |
| Distribution    | operating_systems.add_distribution        | True           | False      |
| Distribution    | operating_systems.change_distribution     | True           | False      |
| Distribution    | operating_systems.delete_distribution     | True           | False      |
| Distribution    | operating_systems.view_distribution       | True           | False      |
| Distribution    | operating_systems.viewall_distribution    | True           | False      |

### Operating System Admin

| Model           | Permission full name                      | Has permission | Owned only |
|-----------------|-------------------------------------------|----------------|------------|
| OperatingSystem | operating_systems.add_operatingsystem     | True           | False      |
| OperatingSystem | operating_systems.change_operatingsystem  | True           | False      |
| OperatingSystem | operating_systems.delete_operatingsystem  | True           | False      |
| OperatingSystem | operating_systems.view_operatingsystem    | True           | False      |
| OperatingSystem | operating_systems.viewall_operatingsystem | True           | False      |
| Distribution    | operating_systems.add_distribution        | False          | False      |
| Distribution    | operating_systems.change_distribution     | False          | False      |
| Distribution    | operating_systems.delete_distribution     | False          | False      |
| Distribution    | operating_systems.view_distribution       | False          | False      |
| Distribution    | operating_systems.viewall_distribution    | False          | False      |

### Operating System Owner

| Model           | Permission full name                      | Has permission | Owned only |
|-----------------|-------------------------------------------|----------------|------------|
| OperatingSystem | operating_systems.add_operatingsystem     | True           | True       |
| OperatingSystem | operating_systems.change_operatingsystem  | True           | True       |
| OperatingSystem | operating_systems.delete_operatingsystem  | True           | True       |
| OperatingSystem | operating_systems.view_operatingsystem    | True           | True       |
| OperatingSystem | operating_systems.viewall_operatingsystem | True           | True       |
| Distribution    | operating_systems.add_distribution        | False          | False      |
| Distribution    | operating_systems.change_distribution     | False          | False      |
| Distribution    | operating_systems.delete_distribution     | False          | False      |
| Distribution    | operating_systems.view_distribution       | False          | False      |
| Distribution    | operating_systems.viewall_distribution    | False          | False      |

### Operating System Add

| Model           | Permission full name                      | Has permission | Owned only |
|-----------------|-------------------------------------------|----------------|------------|
| OperatingSystem | operating_systems.add_operatingsystem     | True           | False      |
| OperatingSystem | operating_systems.change_operatingsystem  | False          | False      |
| OperatingSystem | operating_systems.delete_operatingsystem  | False          | False      |
| OperatingSystem | operating_systems.view_operatingsystem    | False          | False      |
| OperatingSystem | operating_systems.viewall_operatingsystem | False          | False      |
| Distribution    | operating_systems.add_distribution        | False          | False      |
| Distribution    | operating_systems.change_distribution     | False          | False      |
| Distribution    | operating_systems.delete_distribution     | False          | False      |
| Distribution    | operating_systems.view_distribution       | False          | False      |
| Distribution    | operating_systems.viewall_distribution    | False          | False      |

### Operating System Add Owned Only

| Model           | Permission full name                      | Has permission | Owned only |
|-----------------|-------------------------------------------|----------------|------------|
| OperatingSystem | operating_systems.add_operatingsystem     | True           | True       |
| OperatingSystem | operating_systems.change_operatingsystem  | False          | False      |
| OperatingSystem | operating_systems.delete_operatingsystem  | False          | False      |
| OperatingSystem | operating_systems.view_operatingsystem    | False          | False      |
| OperatingSystem | operating_systems.viewall_operatingsystem | False          | False      |
| Distribution    | operating_systems.add_distribution        | False          | False      |
| Distribution    | operating_systems.change_distribution     | False          | False      |
| Distribution    | operating_systems.delete_distribution     | False          | False      |
| Distribution    | operating_systems.view_distribution       | False          | False      |
| Distribution    | operating_systems.viewall_distribution    | False          | False      |

### Operating System Change

| Model           | Permission full name                      | Has permission | Owned only |
|-----------------|-------------------------------------------|----------------|------------|
| OperatingSystem | operating_systems.add_operatingsystem     | False          | False      |
| OperatingSystem | operating_systems.change_operatingsystem  | True           | False      |
| OperatingSystem | operating_systems.delete_operatingsystem  | False          | False      |
| OperatingSystem | operating_systems.view_operatingsystem    | False          | False      |
| OperatingSystem | operating_systems.viewall_operatingsystem | False          | False      |
| Distribution    | operating_systems.add_distribution        | False          | False      |
| Distribution    | operating_systems.change_distribution     | False          | False      |
| Distribution    | operating_systems.delete_distribution     | False          | False      |
| Distribution    | operating_systems.view_distribution       | False          | False      |
| Distribution    | operating_systems.viewall_distribution    | False          | False      |

### Operating System Change Owned Only

| Model           | Permission full name                      | Has permission | Owned only |
|-----------------|-------------------------------------------|----------------|------------|
| OperatingSystem | operating_systems.add_operatingsystem     | False          | False      |
| OperatingSystem | operating_systems.change_operatingsystem  | True           | True       |
| OperatingSystem | operating_systems.delete_operatingsystem  | False          | False      |
| OperatingSystem | operating_systems.view_operatingsystem    | False          | False      |
| OperatingSystem | operating_systems.viewall_operatingsystem | False          | False      |
| Distribution    | operating_systems.add_distribution        | False          | False      |
| Distribution    | operating_systems.change_distribution     | False          | False      |
| Distribution    | operating_systems.delete_distribution     | False          | False      |
| Distribution    | operating_systems.view_distribution       | False          | False      |
| Distribution    | operating_systems.viewall_distribution    | False          | False      |

### Operating System Delete

| Model           | Permission full name                      | Has permission | Owned only |
|-----------------|-------------------------------------------|----------------|------------|
| OperatingSystem | operating_systems.add_operatingsystem     | False          | False      |
| OperatingSystem | operating_systems.change_operatingsystem  | False          | False      |
| OperatingSystem | operating_systems.delete_operatingsystem  | True           | False      |
| OperatingSystem | operating_systems.view_operatingsystem    | False          | False      |
| OperatingSystem | operating_systems.viewall_operatingsystem | False          | False      |
| Distribution    | operating_systems.add_distribution        | False          | False      |
| Distribution    | operating_systems.change_distribution     | False          | False      |
| Distribution    | operating_systems.delete_distribution     | False          | False      |
| Distribution    | operating_systems.view_distribution       | False          | False      |
| Distribution    | operating_systems.viewall_distribution    | False          | False      |

### Operating System Delete Owned Only

| Model           | Permission full name                      | Has permission | Owned only |
|-----------------|-------------------------------------------|----------------|------------|
| OperatingSystem | operating_systems.add_operatingsystem     | False          | False      |
| OperatingSystem | operating_systems.change_operatingsystem  | False          | False      |
| OperatingSystem | operating_systems.delete_operatingsystem  | True           | True       |
| OperatingSystem | operating_systems.view_operatingsystem    | False          | False      |
| OperatingSystem | operating_systems.viewall_operatingsystem | False          | False      |
| Distribution    | operating_systems.add_distribution        | False          | False      |
| Distribution    | operating_systems.change_distribution     | False          | False      |
| Distribution    | operating_systems.delete_distribution     | False          | False      |
| Distribution    | operating_systems.view_distribution       | False          | False      |
| Distribution    | operating_systems.viewall_distribution    | False          | False      |

### Operating System View

| Model           | Permission full name                      | Has permission | Owned only |
|-----------------|-------------------------------------------|----------------|------------|
| OperatingSystem | operating_systems.add_operatingsystem     | False          | False      |
| OperatingSystem | operating_systems.change_operatingsystem  | False          | False      |
| OperatingSystem | operating_systems.delete_operatingsystem  | False          | False      |
| OperatingSystem | operating_systems.view_operatingsystem    | True           | False      |
| OperatingSystem | operating_systems.viewall_operatingsystem | False          | False      |
| Distribution    | operating_systems.add_distribution        | False          | False      |
| Distribution    | operating_systems.change_distribution     | False          | False      |
| Distribution    | operating_systems.delete_distribution     | False          | False      |
| Distribution    | operating_systems.view_distribution       | False          | False      |
| Distribution    | operating_systems.viewall_distribution    | False          | False      |

### Operating System View Owned Only

| Model           | Permission full name                      | Has permission | Owned only |
|-----------------|-------------------------------------------|----------------|------------|
| OperatingSystem | operating_systems.add_operatingsystem     | False          | False      |
| OperatingSystem | operating_systems.change_operatingsystem  | False          | False      |
| OperatingSystem | operating_systems.delete_operatingsystem  | False          | False      |
| OperatingSystem | operating_systems.view_operatingsystem    | True           | True       |
| OperatingSystem | operating_systems.viewall_operatingsystem | False          | False      |
| Distribution    | operating_systems.add_distribution        | False          | False      |
| Distribution    | operating_systems.change_distribution     | False          | False      |
| Distribution    | operating_systems.delete_distribution     | False          | False      |
| Distribution    | operating_systems.view_distribution       | False          | False      |
| Distribution    | operating_systems.viewall_distribution    | False          | False      |

### Operating System View All

| Model           | Permission full name                      | Has permission | Owned only |
|-----------------|-------------------------------------------|----------------|------------|
| OperatingSystem | operating_systems.add_operatingsystem     | False          | False      |
| OperatingSystem | operating_systems.change_operatingsystem  | False          | False      |
| OperatingSystem | operating_systems.delete_operatingsystem  | False          | False      |
| OperatingSystem | operating_systems.view_operatingsystem    | False          | False      |
| OperatingSystem | operating_systems.viewall_operatingsystem | True           | False      |
| Distribution    | operating_systems.add_distribution        | False          | False      |
| Distribution    | operating_systems.change_distribution     | False          | False      |
| Distribution    | operating_systems.delete_distribution     | False          | False      |
| Distribution    | operating_systems.view_distribution       | False          | False      |
| Distribution    | operating_systems.viewall_distribution    | False          | False      |

### Operating System View All Owned Only

| Model           | Permission full name                      | Has permission | Owned only |
|-----------------|-------------------------------------------|----------------|------------|
| OperatingSystem | operating_systems.add_operatingsystem     | False          | False      |
| OperatingSystem | operating_systems.change_operatingsystem  | False          | False      |
| OperatingSystem | operating_systems.delete_operatingsystem  | False          | False      |
| OperatingSystem | operating_systems.view_operatingsystem    | False          | False      |
| OperatingSystem | operating_systems.viewall_operatingsystem | True           | True       |
| Distribution    | operating_systems.add_distribution        | False          | False      |
| Distribution    | operating_systems.change_distribution     | False          | False      |
| Distribution    | operating_systems.delete_distribution     | False          | False      |
| Distribution    | operating_systems.view_distribution       | False          | False      |
| Distribution    | operating_systems.viewall_distribution    | False          | False      |

### Distribution Add

| Model           | Permission full name                      | Has permission | Owned only |
|-----------------|-------------------------------------------|----------------|------------|
| OperatingSystem | operating_systems.add_operatingsystem     | False          | False      |
| OperatingSystem | operating_systems.change_operatingsystem  | False          | False      |
| OperatingSystem | operating_systems.delete_operatingsystem  | False          | False      |
| OperatingSystem | operating_systems.view_operatingsystem    | False          | False      |
| OperatingSystem | operating_systems.viewall_operatingsystem | False          | False      |
| Distribution    | operating_systems.add_distribution        | True           | False      |
| Distribution    | operating_systems.change_distribution     | False          | False      |
| Distribution    | operating_systems.delete_distribution     | False          | False      |
| Distribution    | operating_systems.view_distribution       | False          | False      |
| Distribution    | operating_systems.viewall_distribution    | False          | False      |

### Distribution Add Owned Only

| Model           | Permission full name                      | Has permission | Owned only |
|-----------------|-------------------------------------------|----------------|------------|
| OperatingSystem | operating_systems.add_operatingsystem     | False          | False      |
| OperatingSystem | operating_systems.change_operatingsystem  | False          | False      |
| OperatingSystem | operating_systems.delete_operatingsystem  | False          | False      |
| OperatingSystem | operating_systems.view_operatingsystem    | False          | False      |
| OperatingSystem | operating_systems.viewall_operatingsystem | False          | False      |
| Distribution    | operating_systems.add_distribution        | True           | True       |
| Distribution    | operating_systems.change_distribution     | False          | False      |
| Distribution    | operating_systems.delete_distribution     | False          | False      |
| Distribution    | operating_systems.view_distribution       | False          | False      |
| Distribution    | operating_systems.viewall_distribution    | False          | False      |

### Distribution Change

| Model           | Permission full name                      | Has permission | Owned only |
|-----------------|-------------------------------------------|----------------|------------|
| OperatingSystem | operating_systems.add_operatingsystem     | False          | False      |
| OperatingSystem | operating_systems.change_operatingsystem  | False          | False      |
| OperatingSystem | operating_systems.delete_operatingsystem  | False          | False      |
| OperatingSystem | operating_systems.view_operatingsystem    | False          | False      |
| OperatingSystem | operating_systems.viewall_operatingsystem | False          | False      |
| Distribution    | operating_systems.add_distribution        | False          | False      |
| Distribution    | operating_systems.change_distribution     | True           | False      |
| Distribution    | operating_systems.delete_distribution     | False          | False      |
| Distribution    | operating_systems.view_distribution       | False          | False      |
| Distribution    | operating_systems.viewall_distribution    | False          | False      |

### Distribution Change Owned Only

| Model           | Permission full name                      | Has permission | Owned only |
|-----------------|-------------------------------------------|----------------|------------|
| OperatingSystem | operating_systems.add_operatingsystem     | False          | False      |
| OperatingSystem | operating_systems.change_operatingsystem  | False          | False      |
| OperatingSystem | operating_systems.delete_operatingsystem  | False          | False      |
| OperatingSystem | operating_systems.view_operatingsystem    | False          | False      |
| OperatingSystem | operating_systems.viewall_operatingsystem | False          | False      |
| Distribution    | operating_systems.add_distribution        | False          | False      |
| Distribution    | operating_systems.change_distribution     | True           | True       |
| Distribution    | operating_systems.delete_distribution     | False          | False      |
| Distribution    | operating_systems.view_distribution       | False          | False      |
| Distribution    | operating_systems.viewall_distribution    | False          | False      |

### Distribution Delete

| Model           | Permission full name                      | Has permission | Owned only |
|-----------------|-------------------------------------------|----------------|------------|
| OperatingSystem | operating_systems.add_operatingsystem     | False          | False      |
| OperatingSystem | operating_systems.change_operatingsystem  | False          | False      |
| OperatingSystem | operating_systems.delete_operatingsystem  | False          | False      |
| OperatingSystem | operating_systems.view_operatingsystem    | False          | False      |
| OperatingSystem | operating_systems.viewall_operatingsystem | False          | False      |
| Distribution    | operating_systems.add_distribution        | False          | False      |
| Distribution    | operating_systems.change_distribution     | False          | False      |
| Distribution    | operating_systems.delete_distribution     | True           | False      |
| Distribution    | operating_systems.view_distribution       | False          | False      |
| Distribution    | operating_systems.viewall_distribution    | False          | False      |

### Distribution Delete Owned Only

| Model           | Permission full name                      | Has permission | Owned only |
|-----------------|-------------------------------------------|----------------|------------|
| OperatingSystem | operating_systems.add_operatingsystem     | False          | False      |
| OperatingSystem | operating_systems.change_operatingsystem  | False          | False      |
| OperatingSystem | operating_systems.delete_operatingsystem  | False          | False      |
| OperatingSystem | operating_systems.view_operatingsystem    | False          | False      |
| OperatingSystem | operating_systems.viewall_operatingsystem | False          | False      |
| Distribution    | operating_systems.add_distribution        | False          | False      |
| Distribution    | operating_systems.change_distribution     | False          | False      |
| Distribution    | operating_systems.delete_distribution     | True           | True       |
| Distribution    | operating_systems.view_distribution       | False          | False      |
| Distribution    | operating_systems.viewall_distribution    | False          | False      |

### Distribution View

| Model           | Permission full name                      | Has permission | Owned only |
|-----------------|-------------------------------------------|----------------|------------|
| OperatingSystem | operating_systems.add_operatingsystem     | False          | False      |
| OperatingSystem | operating_systems.change_operatingsystem  | False          | False      |
| OperatingSystem | operating_systems.delete_operatingsystem  | False          | False      |
| OperatingSystem | operating_systems.view_operatingsystem    | False          | False      |
| OperatingSystem | operating_systems.viewall_operatingsystem | False          | False      |
| Distribution    | operating_systems.add_distribution        | False          | False      |
| Distribution    | operating_systems.change_distribution     | False          | False      |
| Distribution    | operating_systems.delete_distribution     | False          | False      |
| Distribution    | operating_systems.view_distribution       | True           | False      |
| Distribution    | operating_systems.viewall_distribution    | False          | False      |

### Distribution View Owned Only

| Model           | Permission full name                      | Has permission | Owned only |
|-----------------|-------------------------------------------|----------------|------------|
| OperatingSystem | operating_systems.add_operatingsystem     | False          | False      |
| OperatingSystem | operating_systems.change_operatingsystem  | False          | False      |
| OperatingSystem | operating_systems.delete_operatingsystem  | False          | False      |
| OperatingSystem | operating_systems.view_operatingsystem    | False          | False      |
| OperatingSystem | operating_systems.viewall_operatingsystem | False          | False      |
| Distribution    | operating_systems.add_distribution        | False          | False      |
| Distribution    | operating_systems.change_distribution     | False          | False      |
| Distribution    | operating_systems.delete_distribution     | False          | False      |
| Distribution    | operating_systems.view_distribution       | True           | True       |
| Distribution    | operating_systems.viewall_distribution    | False          | False      |

### Distribution View All

| Model           | Permission full name                      | Has permission | Owned only |
|-----------------|-------------------------------------------|----------------|------------|
| OperatingSystem | operating_systems.add_operatingsystem     | False          | False      |
| OperatingSystem | operating_systems.change_operatingsystem  | False          | False      |
| OperatingSystem | operating_systems.delete_operatingsystem  | False          | False      |
| OperatingSystem | operating_systems.view_operatingsystem    | False          | False      |
| OperatingSystem | operating_systems.viewall_operatingsystem | False          | False      |
| Distribution    | operating_systems.add_distribution        | False          | False      |
| Distribution    | operating_systems.change_distribution     | False          | False      |
| Distribution    | operating_systems.delete_distribution     | False          | False      |
| Distribution    | operating_systems.view_distribution       | False          | False      |
| Distribution    | operating_systems.viewall_distribution    | True           | False      |

### Distribution View All Owned Only

| Model           | Permission full name                      | Has permission | Owned only |
|-----------------|-------------------------------------------|----------------|------------|
| OperatingSystem | operating_systems.add_operatingsystem     | False          | False      |
| OperatingSystem | operating_systems.change_operatingsystem  | False          | False      |
| OperatingSystem | operating_systems.delete_operatingsystem  | False          | False      |
| OperatingSystem | operating_systems.view_operatingsystem    | False          | False      |
| OperatingSystem | operating_systems.viewall_operatingsystem | False          | False      |
| Distribution    | operating_systems.add_distribution        | False          | False      |
| Distribution    | operating_systems.change_distribution     | False          | False      |
| Distribution    | operating_systems.delete_distribution     | False          | False      |
| Distribution    | operating_systems.view_distribution       | False          | False      |
| Distribution    | operating_systems.viewall_distribution    | True           | True       |

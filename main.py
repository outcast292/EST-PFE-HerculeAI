



if obj_detect == 'banane':
    pickup()

    if picked_up is True: 
        moveToDropLocation(banane)
        if arrivedAtDropLocation is True:
            drop()
    else 
        pickup()

if obj_detect == 'orange':
    pickup()

    if picked_up is True: 
        moveToDropLocation(orange)
        if arrivedAtDropLocation is True:
            drop()
    else 
        pickup()


if obj_detect == 'apple':
    pickup()

    if picked_up is True: 
        moveToDropLocation(apple)
        if arrivedAtDropLocation is True:
            drop()
    else 
        pickup()


This is folder consists of Demo related items

## Notification Panel

### create a collection notifications

#### Table Structure
    id
    category
    sub_category
    user_id
    item
    created_at
    updated_at
    deleted_at
    is_read

#### Mutations
    createNofication(user_id, catgory, sub_Category, item)
    createNofications(user_id, catgory, sub_Category, itemArray)
    updateNofication(id, catgory, sub_Category, item, status)

#### Query
    getUnReadUserNotifications
    getLastReadUserNotification
    getNotificationsByCategory
    getNotificationsByCategorySubCategory

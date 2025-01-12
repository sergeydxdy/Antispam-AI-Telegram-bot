from database.models import session
from database.models import User
from sqlalchemy import select, update, delete, desc


async def set_user(user_data):
    user_id = user_data['user_id']
    username = user_data['username']
    first_name = user_data['first_name']
    last_name = user_data['last_name']
    date = user_data['date']
    async with session() as ses:
        users = await ses.execute(select(User).where(User.user_id == user_id))
        users = users.scalars().all()

        for user in users:
            if (user.username == username and
                    user.first_name == first_name and
                    user.last_name == last_name):
                return

        new_user = User(
            user_id=user_id,
            username=username,
            first_name=first_name,
            last_name=last_name,
            date=date
        )
        ses.add(new_user)
        await ses.commit()

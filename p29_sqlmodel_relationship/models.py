from sqlmodel import Field, SQLModel, Relationship

# both primary key will create composit key
class UserAddressLink(SQLModel, table=True):
    user_id: int = Field(foreign_key="user.id", primary_key=True, ondelete="CASCADE")
    address_id: int = Field(foreign_key="address.id", primary_key=True, ondelete="CASCADE")

class User(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    email: str
    profile: "Profile" = Relationship(back_populates="user", cascade_delete=True) # called relationship attribute. back_populates="user" is Profile table user field
    posts: list["Post"] | None = Relationship(back_populates="user") # called relationship attribute. back_populates="user" is Post model user field
    address: list["Address"] = Relationship(back_populates="user", link_model=UserAddressLink, cascade_delete=True)

# One to one 
class Profile(SQLModel, table=True):
    id: int = Field(primary_key=True)
    user_id: int = Field(foreign_key="user.id", unique=True, ondelete="CASCADE")
    bio: str
    user: "User" = Relationship(back_populates="profile") # called relationship attribute. back_populates="profile" is User model profile field

# One to many
class Post(SQLModel, table=True):
    id: int = Field(primary_key=True)
    user_id: int = Field(foreign_key="user.id", ondelete="SET NULL", nullable=True)
    title: str 
    content: str
    user: "User" = Relationship(back_populates="posts") # called relationship attribute. back_populates="posts" is User mode posts field

# Many to Many
class Address(SQLModel, table=True):
    id: int = Field(primary_key=True)
    street: str
    city: str
    user: list["User"] = Relationship(back_populates="address", link_model=UserAddressLink, cascade_delete=True)
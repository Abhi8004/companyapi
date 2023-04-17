from django.contrib.auth.base_user import BaseUserManager

#abhi123@gmail.com
#ABHI123@gmail.com

class UserManager(BaseUserManager):
    use_in_migrations=True

    def create_user(self,email,password=None,**extrafields):

        if not email:
            raise ValueError('Email is require')

        email=self.normalize_email(email)
        user=self.model(email=email, **extrafields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self,email,password,**extrafields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Super User must have is_staff True'))

        return self.create_user(email,password,**extrafields)

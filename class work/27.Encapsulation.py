##

class Profile:
    def __init__(self,username,password):
        self._followers=set()
        self._following=set()
        self.posts=[]
        self.username=username
        self.__password=password
        self.bio=''
        print(f'\n{self.username}, Your account is created. Have fun with Instagram')

    def getPassword(self):
        return self.__password

    def setPassword(self,new_password):
        self.__password=new_password

    @property
    def NRfollowers(self):
        return self._followers

    @NRfollowers.setter
    def NRfollowers(self,req_uname):
        self._followers.add(req_uname)
        

    @property
    def NRfollowing(self):
        return self._following

    @NRfollowing.setter
    def NRfollowing(self,rai_uname):
        self._following.add(rai_uname)

keerthana= Profile('Keerthana','ker123')

print('Keerthana Details'.center(40,'-'))

print('\nBefore Changing')
print(f'Before Username: {keerthana.username}')
print(f'Before Password: {keerthana.getPassword()}')
print(f'Before Bio: {keerthana.bio}')
print(f'Before Posts: {keerthana.posts}')
print(f'Before Followers: {keerthana.NRfollowers}')
print(f'Before Following: {keerthana.NRfollowing}')

print('\nAfter Changing')
keerthana.username='skeerthana'
print(f'After Username: {keerthana.username}')

keerthana.setPassword('Keerthan@123')
print(f'After Password: {keerthana.getPassword()}')

keerthana.bio='Blogger'
print(f'After Bio: {keerthana.bio}')

keerthana.posts.extend(['Graduation.png','Fest.png','Travalling.mp4'])
print(f'After Posts: {keerthana.posts}')

keerthana.NRfollowers='nihitha'
keerthana.NRfollowers='leorah'
keerthana.NRfollowers='sowmya'
print(f'After Followers: {keerthana.NRfollowers}')

keerthana.NRfollowing='meghana'
keerthana.NRfollowing='maheswari'
keerthana.NRfollowing='revathi'
keerthana.NRfollowing='sunitha'
keerthana.NRfollowing='priyanka'
print(f'After Following: {keerthana.NRfollowing}')


nihitha= Profile('Nihitha','Nih876')
print('Nihitha Details'.center(40,'-'))
print(f'Username: {nihitha.username}')
print(f'Password: {nihitha.getPassword()}')
print(f'Bio: {nihitha.bio}')
print(f'Posts: {nihitha.posts}')
print(f'Followers: {nihitha.NRfollowers}')
print(f'Following: {nihitha.NRfollowing}')

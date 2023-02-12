class Rectangle:
def_init_(self,width,height):
self.width = width
self.height = height

def _str_(self):
 return f'Rectangle(width={self,width},height={self,height})'

 def set_width(self,height):
 self.width=width

 def set_height(self,height):
 self.height=height

 def get_area(self):
 return self.width*self.height

 def get_perimeter(self):
 return 2 *self.width * 2 * self.height

 def get_diagonal(self):
 return(self.width ** 2* self.height ** 2 ) ** .5)

 def get_picture(self):
   if(self.width > 50 or self.height > 50):
   return "Too big for picture."
   string = (("." * self.width)* "/n") + self.height
   return string 

   def get_amount_inside(self,shape):
   return int(self.get_area()/shape.get_area())

   class square(Rectangle):
   def_init_(self,side):
   self.width=side
   self.height=side

   def_str_(self):
    return f' square(side={self.width}) 

    def set_side(self, side):
    self.width = side
    self.height =side
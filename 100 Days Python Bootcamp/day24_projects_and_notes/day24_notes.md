
### Files, Directories, and Paths

This is the one of the first steps of the automating with Python.
After finishing the 100 days I will read the book called `"Automate Boring Stuff with Python" by Al Sweigart.`
First thing we are going to look at is files and file manipulation with Python.

#### Files
Python in itself has a method called `open("a_file_name.its_type(.txt,.py eg.)")`
It will open the file in the code. And `read()` method will return its content as a _string_ object.

When you use _open()_ method python use your computers resources to keep it open. But if you don't close the file it will
close itself when it's absolutely necessary to save resource, but we don't want that because its inefficiency.So when we open the file
and after the necessary operations we should close it, and we are going to make it happen with `close()` method.
```python
file = open("day24_notes.md")
contents = file.read()
print(file)
file.close()
```
It is sounds like so easy, and we are never going to forget to close the file. Wrong! Programmers always do this, look
at your internet browser's open pages, so most of the time instead of using open and manually closing the file
we are going to use `with open("file_name") as 'variable_name'` like this:
```python
with open("day24_notes.md") as file:
    contents = file.read()
    #Do what ever you want to do with the file
    print(contents)
```
As you can see we didn't need to use our `close()` method because when inside the `with` is done file will close itself.

The _open()_'s default is read only so when you want to write something to file you have to change its mode to `"w"` but
that's have a catch. It will delete all the data or thing already exist in the file. So if you don't want to do that, 
just change the mode to `"a"` it's stands for append like in the lists. But these operation only add string objects, don't forget that.  
Example:
```python
with open("day24_text.txt") as file:
    contents = file.read()
    print(contents)
```
Output of my code will be:
> Hello! I am Aidoneus.   
> Nice to meet you.
```python
with open("day24_text.txt",mode="a") as file:
    file.write("\nMy favorite food is caffeine (-_<)")
```
If I run the first code after doing this.Output of my code will be:
> Hello! I am Aidoneus.   
> Nice to meet you.  
> 
> My favorite food is caffeine (-_<)
```python
with open("day24_text.txt",mode="w") as file:
    file.write("My favorite food is caffeine (-_<)")
```
If I run the first code after doing this.Output of my code will be:
> My favorite food is caffeine (-_<)

When I run the code in write mode with never existed file. It will create the file for me.

#### Paths
Files can live in folders and folders can live in another folders. And they all live
in computer. But when you want to access a file in a folder in a folder, how can you access to that file.
This where the path system comes to play. Essentially computers do find the files or the folders with the path.
In an MS OS System the root of the most of the files for the OS and users is your `C:drive`
Let's say you have a .ppt file called "talk" in the "project" folder in the "work" folder,
and "work" folder also have .doc file called "report". You know the "work" folder in the root. How do you access the talk.ppt and report.doc?
> To access the report.doc ==> `C:/work/report.doc`  
> To access the talk.ppt ==> `C:/work/project/talk.ppt`

This is how you access a file or folder from the root. But let's say you open the work folder.
In computer speech that's your working directory. If you want to access the report.doc you only need to write to path ==> `./report.doc` and it will open.
But you know there is a talk.ppt in project folder, and you don't want to manually open it so in path write ==> `./project/talk.ppt`
In other scenario that your working directory is project folder, and you want to open report.doc you need to write ==>`../project.doc`
the `../` means you are going to go to parent folder.
import os,sys,glob
import urllib
import urllib2
from pysoup import verify_bones_file

SERVER = "https://geistwagen-hardsun.rhcloud.com/"
LOCK = "geist.lck"

def get_saves_dir():
  if sys.platform == 'win32' or sys.platform == 'cygwin':
    if os.path.isdir("saves"): #Loose folder
      saves = "saves"
    else:
      saves = os.path.expanduser("~/AppData/Roaming/crawl/saves/")
  elif sys.platform == 'darwin':
    saves = os.path.expanduser("~/Library/Application Support/Dungeon Crawl Stone Soup/saves/")
  if sys.platform.startswith('linux'):
    saves = os.path.expanduser("~/.crawl/saves/")
  else:
    saves = os.path.expanduser("~/.crawl/saves/")
  if not os.path.isdir(saves):
      raise Exception("Crawl saves directory not found!")
  if not os.path.isdir(os.path.join(saves,'db'): #That sucker should always be there
      raise Exception("Crawl saves directory appears to be empty")
  return saves      

def check_lock(saves):
  return os.path.exists(os.path.join(saves,LOCK)

def upload_file(bone):
  level = os.path.basename(bone)
  with open(bone,mode='rb') as file:
    data = file.read()
  req = urllib2.Request(SERVER+level, data, {'Content-Type': 'application/octet-stream'})
  req.get_method = lambda: 'PUT'
  try:
    response = urllib2.urlopen(req)
  except:
    return False
  if response.msg == 'OK':
      return True #Upload success
  else:
      return False

def get_exclusions(bones):
  pass

def download_file(exclude):
  pass

def automatic(saves_dir):  
  if not check_lock(saves_dir):
    open(os.path.join(saves_dir,LOCK),'w').close() #geist.lock written
    bones = glob.glob(os.path.join(saves,'bones.*')
    for bone in bones:
        upload_file(bone)
  else:
    last_ran = os.path.getmtime(os.path.join(saves, LOCK))
    os.utime(os.path.join(saves, LOCK))
    bones = glob.glob(os.path.join(saves,'bones.*')
    exclude = get_exclusions(bones)
    for bone in bones:
        if os.path.getmtime(bone) > last_ran:
            if upload_file(bone):
                dl_results = download_file(exclude)
                if dl_results:
                    exclude.append(dl_results)
                    os.remove(bone)

def main(arguments):
  saves_dir = get_saves_dir()
  automatic(saves_dir)

#TODO start crawl

#TODO alternatively upload a bones file and download a bones file

if __name__ == '__main__':
    main(sys.argv[1:])

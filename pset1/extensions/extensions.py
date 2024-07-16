# prompt file name
fn = (input("What is the file name?: ")).strip()

# conditionals
if "." in fn:
    en = fn.rsplit(".", 1)
    fe = en[1].lower()

    match fe:
      case "gif" | "png" :
        print("image/" + fe)
      case "jpg" | "jpeg" :
        print("image/jpeg")
      case "pdf" | "zip" :
        print("application/" + fe)
      case "txt" :
        print("text/plain")
      case _ :
        print("application/octet-stream")

else:
    print("application/octet-stream")

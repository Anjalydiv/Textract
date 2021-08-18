# Import Boto3,the Python SDK for AWS
import boto3 


#Class to initialize textract,read file and convert contents to text
class amazon_textract:
    def __init__(self,accesskey,secretaccesskey,region):          self.textractclient=boto3.client("textract",aws_access_key_id=accesskey,aws_secret_access_key=secretaccesskey,region_name=region)      
    def analyze_document(self,content):
        response=self.textractclient.detect_document_text(Document={'Bytes':content})
        for blocks in response['Blocks']:
            if (blocks['BlockType']=='LINE'):
                 print(blocks['Text'])
    def read_file(self,filename):
        f=open(filename,"rb")
        content=f.read()
        f.close()
        return(content)
SCHEMA = {
  "typeName" : "AWS::DataSync::LocationAzureBlob",
  "description" : "Resource schema for AWS::DataSync::LocationAzureBlob.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-datasync.git",
  "definitions" : {
    "AzureBlobSasConfiguration" : {
      "additionalProperties" : False,
      "description" : "Specifies the shared access signature (SAS) that DataSync uses to access your Azure Blob Storage container.",
      "type" : "object",
      "properties" : {
        "AzureBlobSasToken" : {
          "description" : "Specifies the shared access signature (SAS) token, which indicates the permissions DataSync needs to access your Azure Blob Storage container.",
          "type" : "string",
          "pattern" : "(^.+$)",
          "minLength" : 1,
          "maxLength" : 255
        }
      },
      "required" : [ "AzureBlobSasToken" ]
    },
    "Tag" : {
      "additionalProperties" : False,
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key for an AWS resource tag.",
          "pattern" : "^[a-zA-Z0-9\\s+=._:/-]+$",
          "maxLength" : 256,
          "minLength" : 1
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for an AWS resource tag.",
          "pattern" : "^[a-zA-Z0-9\\s+=._:@/-]+$",
          "maxLength" : 256,
          "minLength" : 1
        }
      },
      "required" : [ "Key", "Value" ]
    }
  },
  "properties" : {
    "AgentArns" : {
      "description" : "The Amazon Resource Names (ARNs) of agents to use for an Azure Blob Location.",
      "type" : "array",
      "items" : {
        "type" : "string",
        "pattern" : "^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\\-0-9]+:[0-9]{12}:agent/agent-[0-9a-z]{17}$",
        "maxLength" : 128
      },
      "minItems" : 1,
      "maxItems" : 4,
      "insertionOrder" : False
    },
    "AzureBlobAuthenticationType" : {
      "description" : "The specific authentication type that you want DataSync to use to access your Azure Blob Container.",
      "type" : "string",
      "enum" : [ "SAS" ],
      "default" : "SAS"
    },
    "AzureBlobSasConfiguration" : {
      "$ref" : "#/definitions/AzureBlobSasConfiguration"
    },
    "AzureBlobContainerUrl" : {
      "description" : "The URL of the Azure Blob container that was described.",
      "type" : "string",
      "pattern" : "^https://[A-Za-z0-9]((.|-+)?[A-Za-z0-9]){0,252}/[a-z0-9](-?[a-z0-9]){2,62}$",
      "maxLength" : 325
    },
    "AzureBlobType" : {
      "description" : "Specifies a blob type for the objects you're transferring into your Azure Blob Storage container.",
      "type" : "string",
      "enum" : [ "BLOCK" ],
      "default" : "BLOCK"
    },
    "AzureAccessTier" : {
      "description" : "Specifies an access tier for the objects you're transferring into your Azure Blob Storage container.",
      "type" : "string",
      "enum" : [ "HOT", "COOL", "ARCHIVE" ],
      "default" : "HOT"
    },
    "Subdirectory" : {
      "description" : "The subdirectory in the Azure Blob Container that is used to read data from the Azure Blob Source Location.",
      "type" : "string",
      "maxLength" : 1024,
      "pattern" : "^[\\p{L}\\p{M}\\p{Z}\\p{S}\\p{N}\\p{P}\\p{C}]*$"
    },
    "Tags" : {
      "description" : "An array of key-value pairs to apply to this resource.",
      "type" : "array",
      "maxItems" : 50,
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "LocationArn" : {
      "description" : "The Amazon Resource Name (ARN) of the Azure Blob Location that is created.",
      "type" : "string",
      "pattern" : "^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$",
      "maxLength" : 128
    },
    "LocationUri" : {
      "description" : "The URL of the Azure Blob Location that was described.",
      "type" : "string",
      "pattern" : "^(azure-blob)://[a-zA-Z0-9./\\-]+$",
      "maxLength" : 4356
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "datasync:TagResource", "datasync:UntagResource", "datasync:ListTagsForResource" ]
  },
  "additionalProperties" : False,
  "required" : [ "AzureBlobAuthenticationType", "AgentArns" ],
  "readOnlyProperties" : [ "/properties/LocationArn", "/properties/LocationUri" ],
  "primaryIdentifier" : [ "/properties/LocationArn" ],
  "writeOnlyProperties" : [ "/properties/Subdirectory", "/properties/AzureBlobSasConfiguration", "/properties/AzureBlobContainerUrl" ],
  "createOnlyProperties" : [ "/properties/AzureBlobContainerUrl" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "datasync:CreateLocationAzureBlob", "datasync:DescribeLocationAzureBlob", "datasync:TagResource", "datasync:ListTagsForResource" ]
    },
    "read" : {
      "permissions" : [ "datasync:DescribeLocationAzureBlob", "datasync:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "datasync:DescribeLocationAzureBlob", "datasync:ListTagsForResource", "datasync:TagResource", "datasync:UntagResource", "datasync:UpdateLocationAzureBlob" ]
    },
    "delete" : {
      "permissions" : [ "datasync:DeleteLocation" ]
    },
    "list" : {
      "permissions" : [ "datasync:ListLocations" ]
    }
  }
}
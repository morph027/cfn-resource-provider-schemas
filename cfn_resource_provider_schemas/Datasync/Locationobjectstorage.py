SCHEMA = {
  "typeName" : "AWS::DataSync::LocationObjectStorage",
  "description" : "Resource schema for AWS::DataSync::LocationObjectStorage.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-datasync.git",
  "definitions" : {
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
    "AccessKey" : {
      "description" : "Optional. The access key is used if credentials are required to access the self-managed object storage server.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 200,
      "pattern" : "^.+$"
    },
    "AgentArns" : {
      "description" : "The Amazon Resource Name (ARN) of the agents associated with the self-managed object storage server location.",
      "type" : "array",
      "items" : {
        "type" : "string",
        "maxLength" : 128,
        "pattern" : "^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\\-0-9]+:[0-9]{12}:agent/agent-[0-9a-z]{17}$"
      },
      "minItems" : 1,
      "maxItems" : 4,
      "insertionOrder" : False
    },
    "BucketName" : {
      "description" : "The name of the bucket on the self-managed object storage server.",
      "type" : "string",
      "maxLength" : 63,
      "minLength" : 3,
      "pattern" : "^[a-zA-Z0-9_\\-\\+\\./\\(\\)\\$\\p{Zs}]+$"
    },
    "SecretKey" : {
      "description" : "Optional. The secret key is used if credentials are required to access the self-managed object storage server.",
      "type" : "string",
      "minLength" : 8,
      "maxLength" : 200,
      "pattern" : "^.+$"
    },
    "ServerCertificate" : {
      "description" : "X.509 PEM content containing a certificate authority or chain to trust.",
      "type" : "string",
      "maxLength" : 32768
    },
    "ServerHostname" : {
      "description" : "The name of the self-managed object storage server. This value is the IP address or Domain Name Service (DNS) name of the object storage server.",
      "type" : "string",
      "maxLength" : 255,
      "pattern" : "^(([a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9\\-]*[A-Za-z0-9])$"
    },
    "ServerPort" : {
      "description" : "The port that your self-managed server accepts inbound network traffic on.",
      "type" : "integer",
      "minimum" : 1,
      "maximum" : 65536
    },
    "ServerProtocol" : {
      "description" : "The protocol that the object storage server uses to communicate.",
      "type" : "string",
      "enum" : [ "HTTPS", "HTTP" ]
    },
    "Subdirectory" : {
      "description" : "The subdirectory in the self-managed object storage server that is used to read data from.",
      "type" : "string",
      "maxLength" : 4096,
      "pattern" : "^[a-zA-Z0-9_\\-\\+\\./\\(\\)\\p{Zs}]*$"
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
      "description" : "The Amazon Resource Name (ARN) of the location that is created.",
      "type" : "string",
      "pattern" : "^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$",
      "maxLength" : 128
    },
    "LocationUri" : {
      "description" : "The URL of the object storage location that was described.",
      "type" : "string",
      "pattern" : "^(efs|nfs|s3|smb|fsxw|object-storage)://[a-zA-Z0-9./\\-]+$",
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
  "required" : [ "AgentArns" ],
  "readOnlyProperties" : [ "/properties/LocationArn", "/properties/LocationUri" ],
  "writeOnlyProperties" : [ "/properties/SecretKey", "/properties/BucketName", "/properties/ServerHostname", "/properties/Subdirectory" ],
  "primaryIdentifier" : [ "/properties/LocationArn" ],
  "createOnlyProperties" : [ "/properties/BucketName" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "datasync:CreateLocationObjectStorage", "datasync:DescribeLocationObjectStorage", "datasync:ListTagsForResource", "datasync:TagResource" ]
    },
    "read" : {
      "permissions" : [ "datasync:DescribeLocationObjectStorage", "datasync:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "datasync:DescribeLocationObjectStorage", "datasync:ListTagsForResource", "datasync:TagResource", "datasync:UntagResource", "datasync:UpdateLocationObjectStorage" ]
    },
    "delete" : {
      "permissions" : [ "datasync:DeleteLocation" ]
    },
    "list" : {
      "permissions" : [ "datasync:ListLocations" ]
    }
  }
}
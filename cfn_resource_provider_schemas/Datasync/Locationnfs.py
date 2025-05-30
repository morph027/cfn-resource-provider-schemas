SCHEMA = {
  "typeName" : "AWS::DataSync::LocationNFS",
  "description" : "Resource schema for AWS::DataSync::LocationNFS",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-datasync.git",
  "definitions" : {
    "MountOptions" : {
      "additionalProperties" : False,
      "description" : "The NFS mount options that DataSync can use to mount your NFS share.",
      "type" : "object",
      "properties" : {
        "Version" : {
          "description" : "The specific NFS version that you want DataSync to use to mount your NFS share.",
          "type" : "string",
          "enum" : [ "AUTOMATIC", "NFS3", "NFS4_0", "NFS4_1" ]
        }
      }
    },
    "OnPremConfig" : {
      "additionalProperties" : False,
      "description" : "Contains a list of Amazon Resource Names (ARNs) of agents that are used to connect an NFS server.",
      "type" : "object",
      "properties" : {
        "AgentArns" : {
          "description" : "ARN(s) of the agent(s) to use for an NFS location.",
          "type" : "array",
          "items" : {
            "type" : "string",
            "pattern" : "^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\\-0-9]+:[0-9]{12}:agent/agent-[0-9a-z]{17}$",
            "maxLength" : 128
          },
          "minItems" : 1,
          "maxItems" : 4,
          "insertionOrder" : False
        }
      },
      "required" : [ "AgentArns" ]
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
    "MountOptions" : {
      "$ref" : "#/definitions/MountOptions",
      "default" : {
        "Version" : "AUTOMATIC"
      }
    },
    "OnPremConfig" : {
      "$ref" : "#/definitions/OnPremConfig"
    },
    "ServerHostname" : {
      "description" : "The name of the NFS server. This value is the IP address or DNS name of the NFS server.",
      "type" : "string",
      "pattern" : "^(([a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9\\-]*[A-Za-z0-9])$",
      "maxLength" : 255
    },
    "Subdirectory" : {
      "description" : "The subdirectory in the NFS file system that is used to read data from the NFS source location or write data to the NFS destination.",
      "type" : "string",
      "maxLength" : 4096,
      "pattern" : "^[a-zA-Z0-9_\\-\\+\\./\\(\\)\\$\\p{Zs}]+$"
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
      "description" : "The Amazon Resource Name (ARN) of the NFS location.",
      "type" : "string",
      "pattern" : "^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$",
      "maxLength" : 128
    },
    "LocationUri" : {
      "description" : "The URL of the NFS location that was described.",
      "type" : "string",
      "pattern" : "^(efs|nfs|s3|smb|fsxw)://[a-zA-Z0-9./\\-]+$",
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
  "required" : [ "OnPremConfig" ],
  "readOnlyProperties" : [ "/properties/LocationArn", "/properties/LocationUri" ],
  "primaryIdentifier" : [ "/properties/LocationArn" ],
  "writeOnlyProperties" : [ "/properties/ServerHostname", "/properties/Subdirectory" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "datasync:CreateLocationNfs", "datasync:DescribeLocationNfs", "datasync:ListTagsForResource", "datasync:TagResource" ]
    },
    "read" : {
      "permissions" : [ "datasync:DescribeLocationNfs", "datasync:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "datasync:DescribeLocationNfs", "datasync:ListTagsForResource", "datasync:TagResource", "datasync:UntagResource", "datasync:UpdateLocationNfs" ]
    },
    "delete" : {
      "permissions" : [ "datasync:DeleteLocation" ]
    },
    "list" : {
      "permissions" : [ "datasync:ListLocations" ]
    }
  }
}
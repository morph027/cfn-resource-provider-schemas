SCHEMA = {
  "typeName" : "AWS::DataSync::LocationHDFS",
  "description" : "Resource schema for AWS::DataSync::LocationHDFS.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-datasync.git",
  "definitions" : {
    "NameNode" : {
      "additionalProperties" : False,
      "description" : "HDFS Name Node IP and port information.",
      "type" : "object",
      "properties" : {
        "Hostname" : {
          "description" : "The DNS name or IP address of the Name Node in the customer's on premises HDFS cluster.",
          "type" : "string",
          "pattern" : "^(([a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9\\-]*[A-Za-z0-9])$",
          "maxLength" : 255
        },
        "Port" : {
          "description" : "The port on which the Name Node is listening on for client requests.",
          "type" : "integer",
          "minimum" : 1,
          "maximum" : 65536
        }
      },
      "required" : [ "Hostname", "Port" ]
    },
    "Tag" : {
      "additionalProperties" : False,
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Key", "Value" ]
    },
    "QopConfiguration" : {
      "additionalProperties" : False,
      "description" : "Configuration information for RPC Protection and Data Transfer Protection. These parameters can be set to AUTHENTICATION, INTEGRITY, or PRIVACY. The default value is PRIVACY.",
      "type" : "object",
      "properties" : {
        "RpcProtection" : {
          "type" : "string",
          "description" : "Configuration for RPC Protection.",
          "enum" : [ "AUTHENTICATION", "INTEGRITY", "PRIVACY", "DISABLED" ],
          "default" : "PRIVACY"
        },
        "DataTransferProtection" : {
          "type" : "string",
          "description" : "Configuration for Data Transfer Protection.",
          "enum" : [ "AUTHENTICATION", "INTEGRITY", "PRIVACY", "DISABLED" ],
          "default" : "PRIVACY"
        }
      }
    }
  },
  "properties" : {
    "NameNodes" : {
      "description" : "An array of Name Node(s) of the HDFS location.",
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/NameNode"
      },
      "minItems" : 1,
      "insertionOrder" : False
    },
    "BlockSize" : {
      "description" : "Size of chunks (blocks) in bytes that the data is divided into when stored in the HDFS cluster.",
      "type" : "integer",
      "format" : "int64",
      "minimum" : 1048576,
      "maximum" : 1073741824
    },
    "ReplicationFactor" : {
      "description" : "Number of copies of each block that exists inside the HDFS cluster.",
      "type" : "integer",
      "format" : "int64",
      "default" : 3,
      "minimum" : 1,
      "maximum" : 512
    },
    "KmsKeyProviderUri" : {
      "description" : "The identifier for the Key Management Server where the encryption keys that encrypt data inside HDFS clusters are stored.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 255,
      "pattern" : "^kms:\\/\\/http[s]?@(([a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9\\-]*[A-Za-z0-9])(;(([a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9\\-]*[A-Za-z0-9]))*:[0-9]{1,5}\\/kms$"
    },
    "QopConfiguration" : {
      "$ref" : "#/definitions/QopConfiguration"
    },
    "AuthenticationType" : {
      "description" : "The authentication mode used to determine identity of user.",
      "type" : "string",
      "enum" : [ "SIMPLE", "KERBEROS" ]
    },
    "SimpleUser" : {
      "description" : "The user name that has read and write permissions on the specified HDFS cluster.",
      "type" : "string",
      "pattern" : "^[_.A-Za-z0-9][-_.A-Za-z0-9]*$",
      "minLength" : 1,
      "maxLength" : 256
    },
    "KerberosPrincipal" : {
      "description" : "The unique identity, or principal, to which Kerberos can assign tickets.",
      "type" : "string",
      "pattern" : "^.+$",
      "minLength" : 1,
      "maxLength" : 256
    },
    "KerberosKeytab" : {
      "description" : "The Base64 string representation of the Keytab file.",
      "type" : "string",
      "maxLength" : 87384
    },
    "KerberosKrb5Conf" : {
      "description" : "The string representation of the Krb5Conf file, or the presigned URL to access the Krb5.conf file within an S3 bucket.",
      "type" : "string",
      "maxLength" : 174764
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
    "AgentArns" : {
      "description" : "ARN(s) of the agent(s) to use for an HDFS location.",
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
    "Subdirectory" : {
      "description" : "The subdirectory in HDFS that is used to read data from the HDFS source location or write data to the HDFS destination.",
      "type" : "string",
      "maxLength" : 4096,
      "pattern" : "^[a-zA-Z0-9_\\-\\+\\./\\(\\)\\$\\p{Zs}]+$"
    },
    "LocationArn" : {
      "description" : "The Amazon Resource Name (ARN) of the HDFS location.",
      "type" : "string",
      "pattern" : "^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$",
      "maxLength" : 128
    },
    "LocationUri" : {
      "description" : "The URL of the HDFS location that was described.",
      "type" : "string",
      "pattern" : "^(efs|nfs|s3|smb|fsxw|hdfs)://[a-zA-Z0-9.:/\\-]+$",
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
  "required" : [ "NameNodes", "AuthenticationType", "AgentArns" ],
  "readOnlyProperties" : [ "/properties/LocationArn", "/properties/LocationUri" ],
  "primaryIdentifier" : [ "/properties/LocationArn" ],
  "writeOnlyProperties" : [ "/properties/Subdirectory", "/properties/KerberosKeytab", "/properties/KerberosKrb5Conf" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "datasync:CreateLocationHdfs", "datasync:DescribeLocationHdfs", "datasync:TagResource", "datasync:ListTagsForResource" ]
    },
    "read" : {
      "permissions" : [ "datasync:DescribeLocationHdfs", "datasync:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "datasync:UpdateLocationHdfs", "datasync:DescribeLocationHdfs", "datasync:ListTagsForResource", "datasync:TagResource", "datasync:UntagResource" ]
    },
    "delete" : {
      "permissions" : [ "datasync:DeleteLocation" ]
    },
    "list" : {
      "permissions" : [ "datasync:ListLocations" ]
    }
  }
}
SCHEMA = {
  "typeName" : "AWS::DataSync::LocationFSxLustre",
  "description" : "Resource schema for AWS::DataSync::LocationFSxLustre.",
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
    "FsxFilesystemArn" : {
      "description" : "The Amazon Resource Name (ARN) for the FSx for Lustre file system.",
      "type" : "string",
      "maxLength" : 128,
      "pattern" : "^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):fsx:[a-z\\-0-9]+:[0-9]{12}:file-system/fs-[0-9a-f]+$"
    },
    "SecurityGroupArns" : {
      "description" : "The ARNs of the security groups that are to use to configure the FSx for Lustre file system.",
      "type" : "array",
      "items" : {
        "type" : "string",
        "maxLength" : 128,
        "pattern" : "^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):ec2:[a-z\\-0-9]*:[0-9]{12}:security-group/sg-[a-f0-9]+$"
      },
      "maxItems" : 5,
      "minItems" : 1,
      "insertionOrder" : False
    },
    "Subdirectory" : {
      "description" : "A subdirectory in the location's path.",
      "type" : "string",
      "maxLength" : 4096,
      "pattern" : "^[a-zA-Z0-9_\\-\\+\\./\\(\\)\\$\\p{Zs}]+$"
    },
    "Tags" : {
      "description" : "An array of key-value pairs to apply to this resource.",
      "type" : "array",
      "maxItems" : 50,
      "minItems" : 0,
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "LocationArn" : {
      "description" : "The Amazon Resource Name (ARN) of the Amazon FSx for Lustre file system location that is created.",
      "type" : "string",
      "pattern" : "^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$",
      "maxLength" : 128
    },
    "LocationUri" : {
      "description" : "The URL of the FSx for Lustre location that was described.",
      "type" : "string",
      "pattern" : "^(efs|nfs|s3|smb|fsxw|hdfs|fsxl)://[a-zA-Z0-9.:/\\-]+$",
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
  "required" : [ "SecurityGroupArns" ],
  "readOnlyProperties" : [ "/properties/LocationArn", "/properties/LocationUri" ],
  "writeOnlyProperties" : [ "/properties/Subdirectory", "/properties/FsxFilesystemArn" ],
  "primaryIdentifier" : [ "/properties/LocationArn" ],
  "createOnlyProperties" : [ "/properties/FsxFilesystemArn", "/properties/SecurityGroupArns" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "datasync:CreateLocationFsxLustre", "datasync:DescribeLocationFsxLustre", "datasync:ListTagsForResource", "datasync:TagResource", "fsx:DescribeFileSystems", "ec2:DescribeNetworkInterfaces", "ec2:DescribeSubnets", "ec2:DescribeSecurityGroups" ]
    },
    "read" : {
      "permissions" : [ "datasync:DescribeLocationFsxLustre", "datasync:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "datasync:DescribeLocationFsxLustre", "datasync:ListTagsForResource", "datasync:UpdateLocationFsxLustre", "datasync:TagResource", "datasync:UntagResource", "fsx:DescribeFileSystems", "ec2:DescribeNetworkInterfaces" ]
    },
    "delete" : {
      "permissions" : [ "datasync:DeleteLocation" ]
    },
    "list" : {
      "permissions" : [ "datasync:ListLocations" ]
    }
  }
}
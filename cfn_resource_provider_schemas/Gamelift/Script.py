SCHEMA = {
  "$schema" : "https://schema.cloudformation.us-east-1.amazonaws.com/provider.definition.schema.v1.json",
  "typeName" : "AWS::GameLift::Script",
  "description" : "The AWS::GameLift::Script resource creates a new script record for your Realtime Servers script. Realtime scripts are JavaScript that provide configuration settings and optional custom game logic for your game. The script is deployed when you create a Realtime Servers fleet to host your game sessions. Script logic is executed during an active game session.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-gamelift.git",
  "tagging" : {
    "taggable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "permissions" : [ "gamelift:ListTagsForResource", "gamelift:TagResource", "gamelift:UntagResource" ]
  },
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length.",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length.",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    },
    "S3Location" : {
      "$comment" : "Contains object details present in the S3 Bucket",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Bucket" : {
          "description" : "An Amazon S3 bucket identifier. This is the name of the S3 bucket.",
          "type" : "string",
          "minLength" : 1
        },
        "Key" : {
          "description" : "The name of the zip file that contains the script files.",
          "type" : "string",
          "minLength" : 1
        },
        "ObjectVersion" : {
          "description" : "The version of the file, if object versioning is turned on for the bucket. Amazon GameLift uses this information when retrieving files from your S3 bucket. To retrieve a specific version of the file, provide an object version. To retrieve the latest version of the file, do not set this parameter.",
          "type" : "string",
          "minLength" : 1
        },
        "RoleArn" : {
          "description" : "The Amazon Resource Name (ARN) for an IAM role that allows Amazon GameLift to access the S3 bucket.",
          "type" : "string",
          "minLength" : 1
        }
      },
      "required" : [ "Bucket", "Key", "RoleArn" ]
    }
  },
  "properties" : {
    "Name" : {
      "type" : "string",
      "description" : "A descriptive label that is associated with a script. Script names do not need to be unique.",
      "minLength" : 1,
      "maxLength" : 1024
    },
    "StorageLocation" : {
      "type" : "object",
      "description" : "The location of the Amazon S3 bucket where a zipped file containing your Realtime scripts is stored. The storage location must specify the Amazon S3 bucket name, the zip file name (the \"key\"), and a role ARN that allows Amazon GameLift to access the Amazon S3 storage location. The S3 bucket must be in the same Region where you want to create a new script. By default, Amazon GameLift uploads the latest version of the zip file; if you have S3 object versioning turned on, you can use the ObjectVersion parameter to specify an earlier version.",
      "$ref" : "#/definitions/S3Location"
    },
    "Version" : {
      "description" : "The version that is associated with a script. Version strings do not need to be unique.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 1024
    },
    "Tags" : {
      "description" : "An array of key-value pairs to apply to this resource.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "maxItems" : 200,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "CreationTime" : {
      "description" : "A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").",
      "type" : "string"
    },
    "Arn" : {
      "description" : "The Amazon Resource Name (ARN) that is assigned to a Amazon GameLift script resource and uniquely identifies it. ARNs are unique across all Regions. In a GameLift script ARN, the resource ID matches the Id value.",
      "pattern" : "^arn:.*:script\\/script-\\S+",
      "type" : "string"
    },
    "Id" : {
      "description" : "A unique identifier for the Realtime script",
      "pattern" : "^script-\\S+",
      "type" : "string"
    },
    "SizeOnDisk" : {
      "description" : "The file size of the uploaded Realtime script, expressed in bytes. When files are uploaded from an S3 location, this value remains at \"0\".",
      "type" : "integer",
      "minimum" : 1
    }
  },
  "additionalProperties" : False,
  "required" : [ "StorageLocation" ],
  "readOnlyProperties" : [ "/properties/Id", "/properties/CreationTime", "/properties/Arn", "/properties/SizeOnDisk" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "gamelift:CreateScript", "gamelift:ListTagsForResource", "gamelift:TagResource", "gamelift:DescribeScript", "iam:PassRole" ]
    },
    "read" : {
      "permissions" : [ "gamelift:DescribeScript", "gamelift:ListScripts", "gamelift:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "gamelift:DeleteScript" ]
    },
    "list" : {
      "permissions" : [ "gamelift:ListScripts", "gamelift:DescribeScript" ]
    },
    "update" : {
      "permissions" : [ "gamelift:DescribeScript", "gamelift:UpdateScript", "gamelift:ListTagsForResource", "gamelift:TagResource", "gamelift:UntagResource", "iam:PassRole" ]
    }
  }
}
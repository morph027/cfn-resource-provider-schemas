SCHEMA = {
  "typeName" : "AWS::AppStream::AppBlock",
  "description" : "Resource Type definition for AWS::AppStream::AppBlock",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-appstream.git",
  "definitions" : {
    "S3Location" : {
      "type" : "object",
      "properties" : {
        "S3Bucket" : {
          "type" : "string"
        },
        "S3Key" : {
          "type" : "string"
        }
      },
      "additionalProperties" : False,
      "required" : [ "S3Bucket" ]
    },
    "ScriptDetails" : {
      "type" : "object",
      "properties" : {
        "ScriptS3Location" : {
          "$ref" : "#/definitions/S3Location"
        },
        "ExecutablePath" : {
          "type" : "string"
        },
        "ExecutableParameters" : {
          "type" : "string"
        },
        "TimeoutInSeconds" : {
          "type" : "integer"
        }
      },
      "additionalProperties" : False,
      "required" : [ "ScriptS3Location", "ExecutablePath", "TimeoutInSeconds" ]
    },
    "Arn" : {
      "type" : "string"
    },
    "Tag" : {
      "oneOf" : [ {
        "type" : "object",
        "properties" : {
          "Key" : {
            "type" : "string"
          },
          "Value" : {
            "type" : "string"
          }
        },
        "required" : [ "Key", "Value" ],
        "additionalProperties" : False
      }, {
        "type" : "object",
        "properties" : {
          "TagKey" : {
            "type" : "string"
          },
          "TagValue" : {
            "type" : "string"
          }
        },
        "required" : [ "TagKey", "TagValue" ],
        "additionalProperties" : False
      } ]
    },
    "PackagingType" : {
      "type" : "string"
    }
  },
  "properties" : {
    "Name" : {
      "type" : "string"
    },
    "Arn" : {
      "$ref" : "#/definitions/Arn"
    },
    "Description" : {
      "type" : "string"
    },
    "DisplayName" : {
      "type" : "string"
    },
    "SourceS3Location" : {
      "$ref" : "#/definitions/S3Location"
    },
    "SetupScriptDetails" : {
      "$ref" : "#/definitions/ScriptDetails"
    },
    "Tags" : {
      "type" : "array",
      "insertionOrder" : False,
      "uniqueItems" : True,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "CreatedTime" : {
      "type" : "string"
    },
    "PackagingType" : {
      "$ref" : "#/definitions/PackagingType"
    },
    "PostSetupScriptDetails" : {
      "$ref" : "#/definitions/ScriptDetails"
    }
  },
  "required" : [ "Name", "SourceS3Location" ],
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags"
  },
  "primaryIdentifier" : [ "/properties/Arn" ],
  "createOnlyProperties" : [ "/properties/Name", "/properties/DisplayName", "/properties/Description", "/properties/SourceS3Location", "/properties/SetupScriptDetails", "/properties/PackagingType", "/properties/PostSetupScriptDetails" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/CreatedTime" ],
  "writeOnlyProperties" : [ "/properties/Tags" ],
  "deprecatedProperties" : [ "/properties/Tags/TagKey", "/properties/Tags/TagValue" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "appstream:CreateAppBlock", "appstream:TagResource", "s3:GetObject", "s3:ListBucket", "s3:GetBucketOwnershipControls" ]
    },
    "read" : {
      "permissions" : [ "appstream:DescribeAppBlocks" ]
    },
    "delete" : {
      "permissions" : [ "appstream:DeleteAppBlock" ]
    }
  }
}
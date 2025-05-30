SCHEMA = {
  "typeName" : "AWS::CodeCommit::Repository",
  "description" : "Resource Type definition for AWS::CodeCommit::Repository",
  "additionalProperties" : False,
  "properties" : {
    "CloneUrlHttp" : {
      "type" : "string"
    },
    "KmsKeyId" : {
      "type" : "string"
    },
    "CloneUrlSsh" : {
      "type" : "string"
    },
    "RepositoryName" : {
      "type" : "string"
    },
    "Triggers" : {
      "type" : "array",
      "uniqueItems" : False,
      "items" : {
        "$ref" : "#/definitions/RepositoryTrigger"
      }
    },
    "Id" : {
      "type" : "string"
    },
    "Arn" : {
      "type" : "string"
    },
    "Code" : {
      "$ref" : "#/definitions/Code"
    },
    "RepositoryDescription" : {
      "type" : "string"
    },
    "Tags" : {
      "type" : "array",
      "uniqueItems" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "Name" : {
      "type" : "string"
    }
  },
  "definitions" : {
    "S3" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ObjectVersion" : {
          "type" : "string"
        },
        "Bucket" : {
          "type" : "string"
        },
        "Key" : {
          "type" : "string"
        }
      },
      "required" : [ "Bucket", "Key" ]
    },
    "Tag" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Value" : {
          "type" : "string"
        },
        "Key" : {
          "type" : "string"
        }
      },
      "required" : [ "Value", "Key" ]
    },
    "RepositoryTrigger" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "CustomData" : {
          "type" : "string"
        },
        "Events" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "type" : "string"
          }
        },
        "Branches" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "type" : "string"
          }
        },
        "DestinationArn" : {
          "type" : "string"
        },
        "Name" : {
          "type" : "string"
        }
      },
      "required" : [ "Events", "DestinationArn", "Name" ]
    },
    "Code" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "S3" : {
          "$ref" : "#/definitions/S3"
        },
        "BranchName" : {
          "type" : "string"
        }
      },
      "required" : [ "S3" ]
    }
  },
  "required" : [ "RepositoryName" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/CloneUrlHttp", "/properties/Id", "/properties/Name", "/properties/CloneUrlSsh", "/properties/Arn" ]
}
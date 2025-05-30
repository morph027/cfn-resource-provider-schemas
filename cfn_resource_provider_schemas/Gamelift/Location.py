SCHEMA = {
  "$schema" : "https://schema.cloudformation.us-east-1.amazonaws.com/provider.definition.schema.v1.json",
  "typeName" : "AWS::GameLift::Location",
  "description" : "The AWS::GameLift::Location resource creates an Amazon GameLift (GameLift) custom location.",
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
    }
  },
  "properties" : {
    "LocationName" : {
      "type" : "string",
      "minLength" : 8,
      "maxLength" : 64,
      "pattern" : "^custom-[A-Za-z0-9\\-]+"
    },
    "LocationArn" : {
      "type" : "string",
      "pattern" : "^arn:.*:location/custom-\\S+"
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
    }
  },
  "additionalProperties" : False,
  "required" : [ "LocationName" ],
  "createOnlyProperties" : [ "/properties/LocationName" ],
  "readOnlyProperties" : [ "/properties/LocationArn" ],
  "primaryIdentifier" : [ "/properties/LocationName" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "gamelift:CreateLocation", "gamelift:ListLocations", "gamelift:ListTagsForResource", "gamelift:TagResource" ]
    },
    "read" : {
      "permissions" : [ "gamelift:ListLocations", "gamelift:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "gamelift:DeleteLocation" ]
    },
    "list" : {
      "permissions" : [ "gamelift:ListLocations" ]
    },
    "update" : {
      "permissions" : [ "gamelift:ListLocations", "gamelift:ListTagsForResource", "gamelift:TagResource", "gamelift:UntagResource" ]
    }
  }
}
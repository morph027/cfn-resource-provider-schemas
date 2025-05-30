SCHEMA = {
  "typeName" : "AWS::Macie::CustomDataIdentifier",
  "description" : "Macie CustomDataIdentifier resource schema",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-macie.git",
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The tag's key."
        },
        "Value" : {
          "type" : "string",
          "description" : "The tag's value."
        }
      },
      "required" : [ "Value", "Key" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Name" : {
      "description" : "Name of custom data identifier.",
      "type" : "string"
    },
    "Description" : {
      "description" : "Description of custom data identifier.",
      "type" : "string"
    },
    "Regex" : {
      "description" : "Regular expression for custom data identifier.",
      "type" : "string"
    },
    "MaximumMatchDistance" : {
      "description" : "Maximum match distance.",
      "type" : "integer"
    },
    "Keywords" : {
      "description" : "Keywords to be matched against.",
      "type" : "array",
      "items" : {
        "type" : "string"
      }
    },
    "IgnoreWords" : {
      "description" : "Words to be ignored.",
      "type" : "array",
      "items" : {
        "type" : "string"
      }
    },
    "Id" : {
      "description" : "Custom data identifier ID.",
      "type" : "string"
    },
    "Arn" : {
      "description" : "Custom data identifier ARN.",
      "type" : "string"
    },
    "Tags" : {
      "description" : "A collection of tags associated with a resource",
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "macie2:TagResource", "macie2:UntagResource" ]
  },
  "required" : [ "Name", "Regex" ],
  "additionalProperties" : False,
  "createOnlyProperties" : [ "/properties/Name", "/properties/Description", "/properties/Regex", "/properties/MaximumMatchDistance", "/properties/Keywords", "/properties/IgnoreWords" ],
  "readOnlyProperties" : [ "/properties/Id", "/properties/Arn" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "additionalIdentifiers" : [ [ "/properties/Arn" ] ],
  "handlers" : {
    "create" : {
      "permissions" : [ "macie2:CreateCustomDataIdentifier", "macie2:GetCustomDataIdentifier", "macie2:TagResource" ]
    },
    "read" : {
      "permissions" : [ "macie2:GetCustomDataIdentifier" ]
    },
    "delete" : {
      "permissions" : [ "macie2:DeleteCustomDataIdentifier" ]
    },
    "list" : {
      "permissions" : [ "macie2:ListCustomDataIdentifiers" ]
    },
    "update" : {
      "permissions" : [ "macie2:TagResource", "macie2:UntagResource", "macie2:GetCustomDataIdentifier" ]
    }
  }
}
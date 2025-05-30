SCHEMA = {
  "typeName" : "AWS::Synthetics::Group",
  "description" : "Resource Type definition for AWS::Synthetics::Group",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-synthetics",
  "properties" : {
    "Name" : {
      "description" : "Name of the group.",
      "type" : "string",
      "pattern" : "^[0-9a-z_\\-]{1,64}$"
    },
    "Id" : {
      "description" : "Id of the group.",
      "type" : "string"
    },
    "Tags" : {
      "type" : "array",
      "uniqueItems" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "minItems" : 0
    },
    "ResourceArns" : {
      "type" : "array",
      "uniqueItems" : True,
      "items" : {
        "$ref" : "#/definitions/ResourceArn"
      },
      "maxItems" : 10
    }
  },
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. ",
          "minLength" : 1,
          "maxLength" : 128,
          "pattern" : "^(?!aws:)([a-zA-Z\\d\\s_.:/=+\\-@]+)$"
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. ",
          "minLength" : 0,
          "maxLength" : 256,
          "pattern" : "^([a-zA-Z\\d\\s_.:/=+\\-@]*)$"
        }
      },
      "required" : [ "Value", "Key" ]
    },
    "ResourceArn" : {
      "type" : "string",
      "description" : "Provide Canary Arn associated with the group.",
      "pattern" : "arn:(aws[a-zA-Z-]*)?:synthetics:[a-z]{2}((-gov)|(-iso(b|e|f?)))?-[a-z]+-\\d{1}:\\d{12}:canary:[0-9a-z_\\-]"
    }
  },
  "required" : [ "Name" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "synthetics:TagResource", "synthetics:UntagResource", "synthetics:ListTagsForResource" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "synthetics:CreateGroup", "synthetics:AssociateResource", "synthetics:TagResource", "synthetics:GetGroup" ]
    },
    "update" : {
      "permissions" : [ "synthetics:AssociateResource", "synthetics:DisassociateResource", "synthetics:TagResource", "synthetics:UntagResource", "synthetics:GetGroup", "synthetics:ListGroupResources" ]
    },
    "read" : {
      "permissions" : [ "synthetics:GetGroup", "synthetics:ListTagsForResource", "synthetics:ListGroupResources" ]
    },
    "delete" : {
      "permissions" : [ "synthetics:DeleteGroup", "synthetics:GetGroup" ]
    },
    "list" : {
      "permissions" : [ "synthetics:ListGroups" ]
    }
  },
  "additionalProperties" : False,
  "createOnlyProperties" : [ "/properties/Name" ],
  "primaryIdentifier" : [ "/properties/Name" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}
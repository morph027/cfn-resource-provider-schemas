SCHEMA = {
  "typeName" : "AWS::Connect::PredefinedAttribute",
  "description" : "Resource Type definition for AWS::Connect::PredefinedAttribute",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-connect",
  "definitions" : {
    "StringList" : {
      "description" : "Predefined attribute values of type string list.",
      "type" : "array",
      "minItems" : 1,
      "maxItems" : 128,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Value"
      }
    },
    "Value" : {
      "description" : "Textual or numeric value that describes an attribute.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 64
    }
  },
  "properties" : {
    "InstanceArn" : {
      "description" : "The identifier of the Amazon Connect instance.",
      "type" : "string",
      "pattern" : "^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*$"
    },
    "Name" : {
      "description" : "The name of the predefined attribute.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 64
    },
    "Values" : {
      "description" : "The values of a predefined attribute.",
      "type" : "object",
      "properties" : {
        "StringList" : {
          "$ref" : "#/definitions/StringList"
        }
      },
      "additionalProperties" : False
    },
    "LastModifiedRegion" : {
      "description" : "Last modified region.",
      "type" : "string",
      "pattern" : "[a-z]{2}(-[a-z]+){1,2}(-[0-9])?"
    },
    "LastModifiedTime" : {
      "description" : "Last modified time.",
      "type" : "number"
    }
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "connect:CreatePredefinedAttribute" ]
    },
    "read" : {
      "permissions" : [ "connect:DescribePredefinedAttribute" ]
    },
    "delete" : {
      "permissions" : [ "connect:DeletePredefinedAttribute" ]
    },
    "update" : {
      "permissions" : [ "connect:UpdatePredefinedAttribute" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "InstanceArn" : {
            "$ref" : "resource-schema.json#/properties/InstanceArn"
          }
        },
        "required" : [ "InstanceArn" ]
      },
      "permissions" : [ "connect:ListPredefinedAttributes" ]
    }
  },
  "additionalProperties" : False,
  "createOnlyProperties" : [ "/properties/InstanceArn", "/properties/Name" ],
  "readOnlyProperties" : [ "/properties/LastModifiedRegion", "/properties/LastModifiedTime" ],
  "tagging" : {
    "taggable" : False
  },
  "primaryIdentifier" : [ "/properties/InstanceArn", "/properties/Name" ],
  "required" : [ "InstanceArn", "Name", "Values" ]
}
SCHEMA = {
  "typeName" : "AWS::WAFRegional::XssMatchSet",
  "description" : "Resource Type definition for AWS::WAFRegional::XssMatchSet",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "XssMatchTuples" : {
      "type" : "array",
      "uniqueItems" : False,
      "items" : {
        "$ref" : "#/definitions/XssMatchTuple"
      }
    },
    "Name" : {
      "type" : "string"
    }
  },
  "definitions" : {
    "XssMatchTuple" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "TextTransformation" : {
          "type" : "string"
        },
        "FieldToMatch" : {
          "$ref" : "#/definitions/FieldToMatch"
        }
      },
      "required" : [ "TextTransformation", "FieldToMatch" ]
    },
    "FieldToMatch" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Type" : {
          "type" : "string"
        },
        "Data" : {
          "type" : "string"
        }
      },
      "required" : [ "Type" ]
    }
  },
  "required" : [ "Name" ],
  "createOnlyProperties" : [ "/properties/Name" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}
SCHEMA = {
  "typeName" : "AWS::Evidently::Feature",
  "description" : "Resource Type definition for AWS::Evidently::Feature.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-evidently",
  "properties" : {
    "Arn" : {
      "type" : "string",
      "pattern" : "arn:[^:]*:[^:]*:[^:]*:[^:]*:project/[-a-zA-Z0-9._]*/feature/[-a-zA-Z0-9._]*",
      "minLength" : 0,
      "maxLength" : 2048
    },
    "Project" : {
      "type" : "string",
      "pattern" : "([-a-zA-Z0-9._]*)|(arn:[^:]*:[^:]*:[^:]*:[^:]*:project/[-a-zA-Z0-9._]*)",
      "minLength" : 0,
      "maxLength" : 2048
    },
    "Name" : {
      "type" : "string",
      "pattern" : "[-a-zA-Z0-9._]*",
      "minLength" : 1,
      "maxLength" : 127
    },
    "Description" : {
      "type" : "string",
      "minLength" : 0,
      "maxLength" : 160
    },
    "EvaluationStrategy" : {
      "type" : "string",
      "enum" : [ "ALL_RULES", "DEFAULT_VARIATION" ]
    },
    "Variations" : {
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : True,
      "items" : {
        "$ref" : "#/definitions/VariationObject"
      },
      "minItems" : 1,
      "maxItems" : 5
    },
    "DefaultVariation" : {
      "type" : "string",
      "pattern" : "[-a-zA-Z0-9._]*",
      "minLength" : 1,
      "maxLength" : 127
    },
    "EntityOverrides" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/EntityOverride"
      },
      "insertionOrder" : False,
      "uniqueItems" : True,
      "minItems" : 0,
      "maxItems" : 2500
    },
    "Tags" : {
      "description" : "An array of key-value pairs to apply to this resource.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "definitions" : {
    "VariationObject" : {
      "type" : "object",
      "properties" : {
        "VariationName" : {
          "type" : "string",
          "pattern" : "[-a-zA-Z0-9._]*",
          "minLength" : 1,
          "maxLength" : 127
        },
        "BooleanValue" : {
          "type" : "boolean"
        },
        "StringValue" : {
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 512
        },
        "LongValue" : {
          "type" : "number"
        },
        "DoubleValue" : {
          "type" : "number"
        }
      },
      "oneOf" : [ {
        "required" : [ "VariationName", "StringValue" ]
      }, {
        "required" : [ "VariationName", "BooleanValue" ]
      }, {
        "required" : [ "VariationName", "LongValue" ]
      }, {
        "required" : [ "VariationName", "DoubleValue" ]
      } ],
      "additionalProperties" : False
    },
    "EntityOverride" : {
      "type" : "object",
      "properties" : {
        "EntityId" : {
          "type" : "string"
        },
        "Variation" : {
          "type" : "string",
          "pattern" : "[-a-zA-Z0-9._]*",
          "minLength" : 1,
          "maxLength" : 127
        }
      },
      "additionalProperties" : False
    },
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "pattern" : "^(?!aws:)[a-zA-Z+-=._:/]+$",
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
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "additionalProperties" : False,
  "required" : [ "Name", "Project", "Variations" ],
  "createOnlyProperties" : [ "/properties/Name", "/properties/Project" ],
  "readOnlyProperties" : [ "/properties/Arn" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "evidently:CreateFeature", "evidently:TagResource", "evidently:GetFeature" ]
    },
    "read" : {
      "permissions" : [ "evidently:GetFeature", "evidently:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "evidently:UpdateFeature", "evidently:ListTagsForResource", "evidently:TagResource", "evidently:UntagResource", "evidently:GetFeature" ]
    },
    "delete" : {
      "permissions" : [ "evidently:DeleteFeature", "evidently:UntagResource", "evidently:GetFeature" ]
    }
  },
  "taggable" : True
}
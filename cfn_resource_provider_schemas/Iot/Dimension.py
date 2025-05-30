SCHEMA = {
  "typeName" : "AWS::IoT::Dimension",
  "description" : "A dimension can be used to limit the scope of a metric used in a security profile for AWS IoT Device Defender.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-iot.git",
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The tag's key.",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "The tag's value.",
          "minLength" : 1,
          "maxLength" : 256
        }
      },
      "required" : [ "Value", "Key" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Name" : {
      "description" : "A unique identifier for the dimension.",
      "type" : "string",
      "pattern" : "[a-zA-Z0-9:_-]+",
      "minLength" : 1,
      "maxLength" : 128
    },
    "Type" : {
      "description" : "Specifies the type of the dimension.",
      "type" : "string",
      "enum" : [ "TOPIC_FILTER" ]
    },
    "StringValues" : {
      "description" : "Specifies the value or list of values for the dimension.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "type" : "string",
        "minLength" : 1,
        "maxLength" : 256
      },
      "minItems" : 1,
      "maxItems" : 5
    },
    "Tags" : {
      "description" : "Metadata that can be used to manage the dimension.",
      "type" : "array",
      "maxItems" : 50,
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "Arn" : {
      "description" : "The ARN (Amazon resource name) of the created dimension.",
      "type" : "string"
    }
  },
  "additionalProperties" : False,
  "primaryIdentifier" : [ "/properties/Name" ],
  "required" : [ "Type", "StringValues" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "iot:TagResource", "iot:UntagResource", "iot:ListTagsForResource" ]
  },
  "createOnlyProperties" : [ "/properties/Name", "/properties/Type" ],
  "readOnlyProperties" : [ "/properties/Arn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "iot:CreateDimension", "iot:TagResource" ]
    },
    "read" : {
      "permissions" : [ "iot:DescribeDimension", "iot:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "iot:UpdateDimension", "iot:ListTagsForResource", "iot:UntagResource", "iot:TagResource" ]
    },
    "delete" : {
      "permissions" : [ "iot:DescribeDimension", "iot:DeleteDimension" ]
    },
    "list" : {
      "permissions" : [ "iot:ListDimensions" ]
    }
  }
}
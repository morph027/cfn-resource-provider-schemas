SCHEMA = {
  "typeName" : "AWS::Rekognition::Collection",
  "description" : "The AWS::Rekognition::Collection type creates an Amazon Rekognition Collection. A collection is a logical grouping of information about detected faces which can later be referenced for searches on the group",
  "sourceUrl" : "https://docs.aws.amazon.com/rekognition/latest/dg/collections.html",
  "definitions" : {
    "Arn" : {
      "$comment" : "Use the `definitions` block to provide shared resource property schemas",
      "type" : "string",
      "maxLength" : 2048,
      "format" : "(^arn:[a-z\\d-]+:rekognition:[a-z\\d-]+:\\d{12}:collection\\/([a-zA-Z0-9_.\\-]+){1,255})"
    },
    "CollectionId" : {
      "description" : "The name of the collection",
      "type" : "string",
      "maxLength" : 255,
      "pattern" : "\\A[a-zA-Z0-9_\\.\\-]+$"
    },
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "maxLength" : 128,
          "pattern" : "\\A(?!aws:)[a-zA-Z0-9+\\-=\\._\\:\\/@]+$"
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "maxLength" : 256,
          "pattern" : "\\A[a-zA-Z0-9+\\-=\\._\\:\\/@]+$"
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Arn" : {
      "$ref" : "#/definitions/Arn"
    },
    "CollectionId" : {
      "$ref" : "#/definitions/CollectionId"
    },
    "Tags" : {
      "description" : "An array of key-value pairs to apply to this resource.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "minItems" : 0,
      "maxItems" : 200,
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
    "permissions" : [ "rekognition:ListTagsForResource", "rekognition:TagResource", "rekognition:UntagResource" ]
  },
  "additionalProperties" : False,
  "required" : [ "CollectionId" ],
  "readOnlyProperties" : [ "/properties/Arn" ],
  "createOnlyProperties" : [ "/properties/CollectionId" ],
  "primaryIdentifier" : [ "/properties/CollectionId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "rekognition:CreateCollection", "rekognition:DescribeCollection", "rekognition:ListTagsForResource", "rekognition:TagResource" ]
    },
    "read" : {
      "permissions" : [ "rekognition:DescribeCollection", "rekognition:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "rekognition:TagResource", "rekognition:UntagResource", "rekognition:DescribeCollection", "rekognition:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "rekognition:DeleteCollection" ]
    },
    "list" : {
      "permissions" : [ "rekognition:ListCollections" ]
    }
  }
}
SCHEMA = {
  "additionalProperties" : False,
  "definitions" : {
    "ImportSource" : {
      "additionalProperties" : False,
      "properties" : {
        "SourceType" : {
          "type" : "string",
          "description" : "The source type of the import source for the key value store."
        },
        "SourceArn" : {
          "type" : "string",
          "description" : "The Amazon Resource Name (ARN) of the import source for the key value store."
        }
      },
      "required" : [ "SourceType", "SourceArn" ],
      "type" : "object",
      "description" : "The import source for the key value store."
    }
  },
  "description" : "The key value store. Use this to separate data from function code, allowing you to update data without having to publish a new version of a function. The key value store holds keys and their corresponding values.",
  "handlers" : {
    "create" : {
      "permissions" : [ "cloudfront:CreateKeyValueStore", "cloudfront:DescribeKeyValueStore", "s3:GetObject", "s3:HeadObject", "s3:GetBucketLocation" ]
    },
    "delete" : {
      "permissions" : [ "cloudfront:DeleteKeyValueStore", "cloudfront:DescribeKeyValueStore" ]
    },
    "list" : {
      "permissions" : [ "cloudfront:ListKeyValueStores" ]
    },
    "read" : {
      "permissions" : [ "cloudfront:DescribeKeyValueStore" ]
    },
    "update" : {
      "permissions" : [ "cloudfront:UpdateKeyValueStore", "cloudfront:DescribeKeyValueStore" ]
    }
  },
  "properties" : {
    "Arn" : {
      "type" : "string",
      "description" : ""
    },
    "Id" : {
      "type" : "string",
      "description" : ""
    },
    "Status" : {
      "type" : "string",
      "description" : ""
    },
    "Name" : {
      "type" : "string",
      "description" : "The name of the key value store."
    },
    "Comment" : {
      "type" : "string",
      "description" : "A comment for the key value store."
    },
    "ImportSource" : {
      "$ref" : "#/definitions/ImportSource",
      "description" : "The import source for the key value store."
    }
  },
  "primaryIdentifier" : [ "/properties/Name" ],
  "createOnlyProperties" : [ "/properties/Name" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/Id", "/properties/Status" ],
  "writeOnlyProperties" : [ "/properties/ImportSource" ],
  "required" : [ "Name" ],
  "tagging" : {
    "cloudFormationSystemTags" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "taggable" : False
  },
  "typeName" : "AWS::CloudFront::KeyValueStore"
}
SCHEMA = {
  "typeName" : "AWS::S3Outposts::BucketPolicy",
  "description" : "Resource Type Definition for AWS::S3Outposts::BucketPolicy",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-s3outposts.git",
  "definitions" : { },
  "properties" : {
    "Bucket" : {
      "description" : "The Amazon Resource Name (ARN) of the specified bucket.",
      "maxLength" : 2048,
      "minLength" : 20,
      "pattern" : "^arn:[^:]+:s3-outposts:[a-zA-Z0-9\\-]+:\\d{12}:outpost\\/[^:]+\\/bucket\\/[^:]+$",
      "type" : "string"
    },
    "PolicyDocument" : {
      "description" : "A policy document containing permissions to add to the specified bucket.",
      "type" : "object"
    }
  },
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "additionalProperties" : False,
  "createOnlyProperties" : [ "/properties/Bucket" ],
  "required" : [ "Bucket", "PolicyDocument" ],
  "primaryIdentifier" : [ "/properties/Bucket" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "s3-outposts:PutBucketPolicy", "s3-outposts:GetBucketPolicy" ]
    },
    "read" : {
      "permissions" : [ "s3-outposts:GetBucketPolicy" ]
    },
    "update" : {
      "permissions" : [ "s3-outposts:PutBucketPolicy", "s3-outposts:GetBucketPolicy" ]
    },
    "delete" : {
      "permissions" : [ "s3-outposts:DeleteBucketPolicy", "s3-outposts:GetBucketPolicy" ]
    }
  }
}
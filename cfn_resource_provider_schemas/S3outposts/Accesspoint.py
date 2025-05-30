SCHEMA = {
  "typeName" : "AWS::S3Outposts::AccessPoint",
  "description" : "Resource Type Definition for AWS::S3Outposts::AccessPoint",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-s3outposts.git",
  "definitions" : {
    "VpcConfiguration" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "VpcId" : {
          "description" : "Virtual Private Cloud (VPC) Id from which AccessPoint will allow requests.",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 1024
        }
      }
    }
  },
  "properties" : {
    "Arn" : {
      "description" : "The Amazon Resource Name (ARN) of the specified AccessPoint.",
      "maxLength" : 2048,
      "minLength" : 20,
      "pattern" : "^arn:[^:]+:s3-outposts:[a-zA-Z0-9\\-]+:\\d{12}:outpost\\/[^:]+\\/accesspoint\\/[^:]+$",
      "type" : "string"
    },
    "Bucket" : {
      "description" : "The Amazon Resource Name (ARN) of the bucket you want to associate this AccessPoint with.",
      "maxLength" : 2048,
      "minLength" : 20,
      "pattern" : "^arn:[^:]+:s3-outposts:[a-zA-Z0-9\\-]+:\\d{12}:outpost\\/[^:]+\\/bucket\\/[^:]+$",
      "type" : "string"
    },
    "Name" : {
      "description" : "A name for the AccessPoint.",
      "maxLength" : 50,
      "minLength" : 3,
      "pattern" : "^[a-z0-9]([a-z0-9\\\\-]*[a-z0-9])?$",
      "type" : "string"
    },
    "VpcConfiguration" : {
      "description" : "Virtual Private Cloud (VPC) from which requests can be made to the AccessPoint.",
      "$ref" : "#/definitions/VpcConfiguration"
    },
    "Policy" : {
      "description" : "The access point policy associated with this access point.",
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
  "required" : [ "Bucket", "Name", "VpcConfiguration" ],
  "createOnlyProperties" : [ "/properties/Bucket", "/properties/Name", "/properties/VpcConfiguration" ],
  "readOnlyProperties" : [ "/properties/Arn" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "s3-outposts:CreateAccessPoint", "s3-outposts:GetAccessPoint", "s3-outposts:PutAccessPointPolicy", "s3-outposts:GetAccessPointPolicy" ]
    },
    "read" : {
      "permissions" : [ "s3-outposts:GetAccessPoint", "s3-outposts:GetAccessPointPolicy" ]
    },
    "update" : {
      "permissions" : [ "s3-outposts:GetAccessPoint", "s3-outposts:PutAccessPointPolicy", "s3-outposts:GetAccessPointPolicy", "s3-outposts:DeleteAccessPointPolicy" ]
    },
    "delete" : {
      "permissions" : [ "s3-outposts:DeleteAccessPoint", "s3-outposts:DeleteAccessPointPolicy" ]
    },
    "list" : {
      "permissions" : [ "s3-outposts:ListAccessPoints" ]
    }
  }
}
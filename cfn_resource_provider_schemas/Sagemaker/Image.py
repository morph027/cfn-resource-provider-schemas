SCHEMA = {
  "typeName" : "AWS::SageMaker::Image",
  "description" : "Resource Type definition for AWS::SageMaker::Image",
  "additionalProperties" : False,
  "properties" : {
    "ImageName" : {
      "$ref" : "#/definitions/ImageName"
    },
    "ImageArn" : {
      "$ref" : "#/definitions/ImageArn"
    },
    "ImageRoleArn" : {
      "$ref" : "#/definitions/ImageRoleArn"
    },
    "ImageDisplayName" : {
      "$ref" : "#/definitions/ImageDisplayName"
    },
    "ImageDescription" : {
      "$ref" : "#/definitions/ImageDescription"
    },
    "Tags" : {
      "type" : "array",
      "maxItems" : 50,
      "description" : "An array of key-value pairs to apply to this resource.",
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "definitions" : {
    "ImageName" : {
      "type" : "string",
      "description" : "The name of the image.",
      "pattern" : "^[a-zA-Z0-9]([-.]?[a-zA-Z0-9])*$",
      "minLength" : 1,
      "maxLength" : 63
    },
    "ImageArn" : {
      "description" : "The Amazon Resource Name (ARN) of the image.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 256,
      "pattern" : "^arn:aws(-[\\w]+)*:sagemaker:[a-z0-9\\-]*:[0-9]{12}:image\\/[a-zA-Z0-9]([-.]?[a-zA-Z0-9])*$"
    },
    "ImageRoleArn" : {
      "description" : "The Amazon Resource Name (ARN) of an IAM role that enables Amazon SageMaker to perform tasks on behalf of the customer.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 256,
      "pattern" : "^arn:aws(-[\\w]+)*:iam::[0-9]{12}:role/.*$"
    },
    "ImageDisplayName" : {
      "type" : "string",
      "description" : "The display name of the image.",
      "pattern" : "^[A-Za-z0-9 -_]+$",
      "minLength" : 1,
      "maxLength" : 128
    },
    "ImageDescription" : {
      "type" : "string",
      "description" : "A description of the image.",
      "pattern" : ".+",
      "minLength" : 1,
      "maxLength" : 512
    },
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. ",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. ",
          "maxLength" : 256
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "required" : [ "ImageName", "ImageRoleArn" ],
  "primaryIdentifier" : [ "/properties/ImageArn" ],
  "additionalIdentifiers" : [ [ "/properties/ImageName" ] ],
  "readOnlyProperties" : [ "/properties/ImageArn" ],
  "createOnlyProperties" : [ "/properties/ImageName" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "sagemaker:CreateImage", "sagemaker:DescribeImage", "iam:PassRole", "sagemaker:AddTags", "sagemaker:ListTags" ]
    },
    "read" : {
      "permissions" : [ "sagemaker:DescribeImage", "sagemaker:ListTags" ]
    },
    "update" : {
      "permissions" : [ "sagemaker:UpdateImage", "sagemaker:DescribeImage", "sagemaker:ListTags", "sagemaker:AddTags", "sagemaker:DeleteTags", "iam:PassRole" ]
    },
    "delete" : {
      "permissions" : [ "sagemaker:DeleteImage", "sagemaker:DescribeImage" ]
    },
    "list" : {
      "permissions" : [ "sagemaker:ListImages" ]
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "sagemaker:AddTags", "sagemaker:ListTags", "sagemaker:DeleteTags" ]
  }
}
SCHEMA = {
  "additionalProperties" : False,
  "definitions" : {
    "CloudFrontOriginAccessIdentityConfig" : {
      "additionalProperties" : False,
      "properties" : {
        "Comment" : {
          "type" : "string",
          "description" : "A comment to describe the origin access identity. The comment cannot be longer than 128 characters."
        }
      },
      "required" : [ "Comment" ],
      "type" : "object",
      "description" : "Origin access identity configuration. Send a ``GET`` request to the ``/CloudFront API version/CloudFront/identity ID/config`` resource."
    }
  },
  "description" : "The request to create a new origin access identity (OAI). An origin access identity is a special CloudFront user that you can associate with Amazon S3 origins, so that you can secure all or just some of your Amazon S3 content. For more information, see [Restricting Access to Amazon S3 Content by Using an Origin Access Identity](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html) in the *Amazon CloudFront Developer Guide*.",
  "handlers" : {
    "create" : {
      "permissions" : [ "cloudfront:CreateCloudFrontOriginAccessIdentity" ]
    },
    "delete" : {
      "permissions" : [ "cloudfront:DeleteCloudFrontOriginAccessIdentity", "cloudfront:GetCloudFrontOriginAccessIdentity" ]
    },
    "list" : {
      "permissions" : [ "cloudfront:ListCloudFrontOriginAccessIdentities" ]
    },
    "read" : {
      "permissions" : [ "cloudfront:GetCloudFrontOriginAccessIdentity" ]
    },
    "update" : {
      "permissions" : [ "cloudfront:UpdateCloudFrontOriginAccessIdentity", "cloudfront:GetCloudFrontOriginAccessIdentity" ]
    }
  },
  "primaryIdentifier" : [ "/properties/Id" ],
  "properties" : {
    "CloudFrontOriginAccessIdentityConfig" : {
      "$ref" : "#/definitions/CloudFrontOriginAccessIdentityConfig",
      "description" : "The current configuration information for the identity."
    },
    "Id" : {
      "type" : "string",
      "description" : ""
    },
    "S3CanonicalUserId" : {
      "type" : "string",
      "description" : ""
    }
  },
  "readOnlyProperties" : [ "/properties/Id", "/properties/S3CanonicalUserId" ],
  "required" : [ "CloudFrontOriginAccessIdentityConfig" ],
  "tagging" : {
    "cloudFormationSystemTags" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "taggable" : False
  },
  "typeName" : "AWS::CloudFront::CloudFrontOriginAccessIdentity"
}
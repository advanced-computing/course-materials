# Google Cloud

## Course setup

This only needs to be done once per semester.

1. If the number of students+instructors is larger than 20, [request a Project Quota increase](https://support.google.com/code/contact/project_quota_increase).
1. [Install Terraform](https://developer.hashicorp.com/terraform/install).
1. [Install `gcloud`](https://cloud.google.com/sdk/docs/install).
1. Set up `gcloud`:

   ```sh
   gcloud config configurations activate columbia
   gcloud auth application-default login
   ```

1. Ensure the [teams list](project_teams.csv) is up to date.
1. Run `terraform apply`.

As students go through the setup (below), you can re-run the `apply` to get a report of who is missing billing.

## Student setup

Do these one-time setup steps to ensure you don't have to pay for Google Cloud use for this class. Credits are provided through the [Google Cloud for Education](https://cloud.google.com/edu/faculty) program.

A [Project](https://cloud.google.com/docs/overview#projects) has been created for you, which the instructors have access to for troubleshooting. You redeem the credits, which creates a Billing Account. You then have to associate that Billing Account with the existing Project.

1. [Redeem the credits](https://cloud.google.com/billing/docs/how-to/edu-grants#redeem) - [video walkthrough](https://www.youtube.com/watch?v=2AnX7BX-qew)
   1. Instructor will send the coupon retrieval link
   1. Fill in the form
      - Use your UNI for your email, not an [alias](https://www.cuit.columbia.edu/email/email-aliases)
   1. When you get to [the GCP Credit Application screen](https://console.cloud.google.com/education), **make sure you've [switched to your Columbia Google account](https://support.google.com/docs/answer/2405894)**
1. [Dismiss the Free Trial banner — should not need a credit card](https://services.google.com/fh/files/helpcenter/cloud_edu_free_trial_warning.pdf)
1. Confirm the credits were applied
   1. Go to [the Billing Accounts page](https://console.cloud.google.com/billing?organizationId=819335046878)
   1. Click `Billing Account for Education`
   1. In the sidebar, click `Credits`
   1. You should see an `Operations Management in IT` credit for $50
1. Switch to your Project
   1. In the top navigation bar, on the left side, click the drop-down
   1. You should see a `Select a resource` modal pop up
   1. Click the `ALL` tab
   1. Click `sipa-adv-c-<name1>-<name2>`
1. [Change the Billing Account](https://cloud.google.com/billing/docs/how-to/modify-project#how-to-change-ba) to `Billing Account for Education`

### Accidentally redeemed the credit with the wrong Google account

If you missed the step above about switching to your Columbia Google account, the easiest fix is to follow [these steps](https://cloud.google.com/billing/docs/how-to/grant-access-to-billing#update-cloud-billing-permissions) and make your `<uni>@columbia.edu` user a `Billing Account Administrator` on the `Billing Account for Education`.

### Use of Google Cloud outside this class

If you're using Google Cloud for something outside of this class, we suggest [creating a separate Project](https://cloud.google.com/resource-manager/docs/creating-managing-projects) to keep things isolated. The `Billing Account for Education` is yours, so you're welcome to [associate it with other Projects](https://cloud.google.com/billing/docs/how-to/modify-project#how-to-change-ba) to use those credits.

We won't use the full $50 credit for this class, so you're welcome to take advantage of the remainder for other things. If you use it up, you'll start spending against your [Free Trial](https://cloud.google.com/free). Beyond that, you'll have to [pay](https://cloud.google.com/billing/docs/how-to/payment-methods).
